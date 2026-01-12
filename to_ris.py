import rispy
from tqdm import tqdm
import pandas as pd
import ast
def export_ris_string(database, file, myname="export"):
    entries = []
    data=pd.read_csv(file).fillna("")
    print(data.shape)
    for i, e in tqdm(data.iterrows()):
        current_entry = {}

        if e.get("type_of_reference", "") != "":
            current_entry["type_of_reference"] = e["type_of_reference"]

        current_entry["name_of_database"] = database

        if e.get("Title", "") != "":
            t=e["Title"].replace("  ", " ")
            current_entry["title"] = t
        if e.get("link_pdf", "") != "":
            current_entry["url"] = e["link_pdf"]
        elif e.get("Url", "") != "":
            current_entry["url"] = e["Url"]

        ##########################pages to ris
        sp = ""
        ep = ""
        if e.get("pages", "") != "":
            pages = [p.strip() for p in e["pages"].split("-")]
            if len(pages) == 2:
                sp = pages[0]
                ep = pages[1]
            else:
                sp = e.get("pages", "")

        if sp != "":
            current_entry["start_page"] = sp
        if ep != "":
            current_entry["end_page"] = ep
        ##############################################
        try:
            if e.get("Year", "") != "":
                current_entry["year"] = int(e["Year"])
        except:
            if e.get("year", "") != "":
                current_entry["year"] = e["year"]

        if e.get("issn", "") != "":
            try:
                current_entry["issn"] = int(e["issn"])
            except:
                current_entry["issn"] = e["issn"]

        if e.get("volume", "") != "":
            try:
                current_entry["volume"] = int(e["volume"])
            except:
                current_entry["volume"] = e["volume"]

        if e.get("Abstract", "") != "":
            current_entry["abstract"] = ' '.join(e["Abstract"].split()).strip()
        if e.get("DOI", "") != "":
            current_entry["doi"] = e["DOI"]
            print("found doi")
        if e.get("pmid", "") != "":
            current_entry["pubmed_id"] = e["pmid"]

        if e.get("number", "") != "":
            try:
                current_entry["number"] = int(e["issue"])
            except:
                current_entry["number"] = e["issue"]
        if e.get("journal", "") != "":
            current_entry["secondary_title"] = e["journal"]
        if e.get("Authors", "") != "":
            astr=e["Authors"]
            if astr.startswith("["):
                x = ast.literal_eval(astr)
                nams=[]
                for n in x:
                    prts=n.split(" ")
                    last=prts[-1]
                    del prts[-1]
                    others=" ".join(prts)
                    thisnam="{}, {}".format(last, others)
                    nams.append(thisnam)
                current_entry["authors"] =nams
            else:
                current_entry["authors"] = [a for a in e["Authors"].split("; ")]

        if e.get("keywords", "") != "":
            current_entry["keywords"] = [k for k in e["keywords"].split("; ")]

        if e.get("place_published", "") != "":
            current_entry["place_published"] = e["place_published"]
        if e.get("Date", "") != "":
            current_entry["date"] = e["Date"]

        if e.get("original_publication", "") != "":
            current_entry["original_publication"] = e["original_publication"]
        if e.get("access_date", "") != "":
            current_entry["access_date"] = e["access_date"]
        if e.get("language", "") != "":
            #
            current_entry["language"] = e["language"]
        if e.get("publisher", "") != "":
            current_entry["publisher"] = 'Association for Computational Linguistics'
        if e.get("ID", "") != "":
            current_entry["id"] = e["ID"]

        if e.get("author_address", "") != "":
            current_entry["author_address"] = e["author_address"]

        if e.get("fulltext_link", "") != "":
            note = "Fulltext: {} ; {}".format(e['fulltext_link'], e.get("other_info", ""))
        else:
            note = e.get("published", "")
        current_entry["label"] = note
        # print(note)

        entries.append(current_entry)

    with open("{}_{}_{}_references.ris".format(database,myname, data.shape[0]), 'w',
                  encoding="utf-8") as bibliography_file:
            rispy.dump(entries, bibliography_file)

export_ris_string("ACL", r"data\results_acl_Nadia_Jan2026.csv", "NADIA")
# export_ris_string("arxiv", r"C:\Users\lena.schmidt\Documents\Suicide_LSR\SR_automation_LSR-master\SR_automation_LSR-master\data\results_arxiv.csv")
# export_ris_string("acl", r"C:\Users\lena.schmidt\Documents\Suicide_LSR\SR_automation_LSR-master\SR_automation_LSR-master\data\results_acl.csv")
#export_ris_string("dblp", r"C:\Users\lena.schmidt\Documents\Suicide_LSR\SR_automation_LSR-master\SR_automation_LSR-master\data\results_dblp.csv")

# export_ris_string("arxiv", r"data\results_arxiv.csv")
# export_ris_string("acl", r"data\results_acl.csv")
# export_ris_string("dblp", r"data\results_dblp.csv")

# import re
# with open("{}_references.ris".format("ACL"), 'r',encoding="utf-8") as bibliography_file:
#     lines=bibliography_file.readlines()
#
#     lines=[l for l in lines if not re.search(r"(LB  - \n)|(\d+\.\n)|(^.+\s\s-)",l)]
#     print(lines)
# with open("{}_references.ris".format("ACL"), 'w',encoding="utf-8") as bibliography_file:
#     bibliography_file.writelines(lines)