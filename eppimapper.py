import json
import rispy


def add_data(refdict, e, eppiname, asname, altname="XYZ"):
    #general function checking presence of an item with option to give alternaticve ris field name.
    # it adds the item if it exists in the ris entry, otherwise empty string is added
    if asname in e.keys():
        refdict[eppiname] = e[asname]
    elif altname in e.keys():
        refdict[eppiname] = e[altname]
    else:
        refdict[eppiname] = ""
    #return refdict#don't actually need to return anything lol

def get_metadata(e):
    refdict = {}
    refdict["Codes"] = []
    refdict["Outcomes"]=[]
    add_data(refdict, e, "ItemId", "id")
    add_data(refdict, e, "Title", "title")
    add_data(refdict, e, "ParentTitle", "secondary_title", altname="alternate_title1")

    add_data(refdict, e, "ShortTitle", "id")
    refdict["DateCreated"] = "09/10/2024"
    refdict["CreatedBy"] = "Lena Schmidt"
    refdict["DateEdited"] = "09/10/2024"
    refdict["EditedBy"] = "Lena Schmidt"

    add_data(refdict, e, "Year", "year")

    refdict["Month"] = ""
    refdict["StandardNumber"] = ""
    refdict["City"] = ""
    refdict["Country"] = ""
    refdict["Publisher"] = ""
    refdict["Institution"] = ""
    add_data(refdict, e, "Volume", "volume")
    pgs = ""
    if 'start_page' in e.keys():
        pgs = e["start_page"]
        if 'end_page' in e.keys():
            pgs = pgs + "-" + e["end_page"]
    elif 'end_page' in e.keys():
        pgs = e["end_page"]
    if pgs != "":
        refdict["Pages"] = pgs
    else:
        refdict["Pages"] =""

    refdict["Edition"] = ""
    add_data(refdict, e, "Issue", "number")
    refdict["Availability"] = ""
    add_data(refdict, e, "URL", "url")

    if refdict["URL"]=="":
        print('https://doi.org/{}'.format(e.get('doi', '')))
    else:
        print(refdict["URL"])

    refdict["OldItemId"] = ""
    add_data(refdict, e, "Abstract", "abstract")
    refdict["Comments"] = ""
    refdict["TypeName"] = "Journal, Article"
    qc=""#quick citation
    if 'authors' in e.keys():
        refdict["Authors"] ="; ".join(e["authors"])
        qc=e["authors"][0]
    else:
        refdict["Authors"] = ""
    refdict["ParentAuthors"] = ""

    add_data(refdict, e, "DOI", "doi")
    refdict["Keywords"] = "eppi-reviewer4"

    refdict["ItemStatus"]= "I"
    refdict["ItemStatusTooltip"]= "Included in review"
    refdict["QuickCitation"] =qc

    return refdict




def read_as(as_data):
    ###########################read data extraction

    reflist=[]#contains dicts that have a list of codes and metadata
    attributeslist=[]#so many attributes lists

    attributes = {'q1 Data extraction approach(es) used, select one or more: ': {},
                  'q3 Reported performance metric(s) used for evaluation: ': {},
                  'q5 Types of data: ': {},
                  'q7 The input data format(s): ': {},
                  'q8 The output data format(s): ': {},
                  'q9 Mined field(s): ': {},
                  'q11 Granularity of data mining: ': {},
                  'q6 Target (study) design(s) for data extraction: ': {},
                  'q16 Can data be retrieved based on the information given in the publication?: ': {},
                  'q17 Is there a description of the dataset used and of its characteristics? ': {},
                  'q24 Can we access source code based on the information in the publication?: ': {},
                  'q26 Is an app available that does the data mining, eg. a web-app or desktop version?: ': {},
                  'q30 Which basic metric(s) are reported (true/false positives and negatives) or can be inferred? Select one or more:: ': {},
                  'LLM Prompt development: ': {},
                  'LLM Repeated trial/simulation runs: is there a description of the results: ': {},
                  'LLM application: ': {},
                  'SWAR?: ': {},
                  'q37 Did the authors assess or share information about model explainability? (question formerly about hidden variables): ': {},
                  'q42 Is the model’s adaptability to different formats and/or environments beyond training and testing data described?: ': {},
                  }

    with open(as_data, 'r', encoding='utf-8') as bibliography_file:
        entries = rispy.load(bibliography_file)
        cnt=1
        for e in entries:
            # for k in e.keys():
            #     print(k, ": ", e[k])
            #     print("")
                ###getting metadata for reflist
            if 'L1.Include this reference?: No, exclude the reference' not in e.get("notes", []):#check if ref is includede and then add attributes
                extraction=[]
                myattributes=[]
                for n in e.get("notes", []):
                    if n.startswith("L1."):
                        extraction.append(n)
                    else:
                        extraction[-1]=extraction[-1] + " " + n
                #print(extraction)

                for x in extraction:#each answer to a qurestion
                    for key, value in attributes.items():#each existing attribute. Key is the name and value is a list of integers
                        if key in x:#if we have an attribute that needs to go to the map
                            x=x.split(key)[1]#get field value
                            xlist=x.split("|")#if there are multiple codes in a field then they are separated by that sign so we need to split them
                            for xl in xlist:#single item, eg P, IC, or O
                                if xl not in value.keys():#we haven't seen that particular code yet so it needs a new ID
                                    value[xl]=cnt
                                    myattributes.append(cnt)
                                    cnt+=1
                                else:
                                    myattributes.append(value[xl])
                # print(myattributes)
                # print("-------------------------")
                refdict = get_metadata(e)
                codelist=[]#
                for att in myattributes:
                    codelist.append({"AttributeId": att,"ItemAttributeFullTextDetails": []})
                refdict["Codes"] =codelist
                #print(refdict)
                reflist.append(refdict)


    for key,value in attributes.items():#reformat attributes list to correct format
        thisattributes=[]
        for k,v in value.items():
            thisattributes.append({"AttributeId": v,
									"AttributeName": k})
        adict={"AttributeId": cnt,
				"AttributeName": key,
				"Attributes": {
                    "AttributesList": thisattributes
                }
               }
        attributeslist.append(adict)
        cnt+=1

    final_json={
        "CodeSets": [
            {
                "SetName": "Mapping tool",
                "Attributes": {
                    "AttributesList": attributeslist
                }
            }
        ],
        "References": reflist
    }

    with open('out/as_data_refs_test.json', 'w', encoding='utf-8') as f:
        json.dump(final_json, f, ensure_ascii=False, indent=4)
    #print(attributes)


as_data=r'C:\Users\lena.schmidt\Documents\SR automation review\Update_2\Refdata.ris'
read_as(as_data)
