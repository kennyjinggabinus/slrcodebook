import json,csv,collections,pathlib

OUT=pathlib.Path(__file__).resolve().parent
OUT.mkdir(parents=True,exist_ok=True)
values=json.loads((OUT/'SLR_Extraction_Snapshot.json').read_text())['values']
headers,rows=values[0],values[1:]
audit=[]
for excel_row,r in enumerate(rows,2):
    sid=r[0]
    scores=[int(r[12] not in ('NR','',None)),int(r[21]=='Y'),0,
            int(sid in ('RPID_46','RPID_47')),int(sid=='RPID_46'),
            int(r[34]=='Yes'),0.5 if sid=='RPID_46' else 0,
            int(sid=='RPID_47'),0]
    notes=[f'G1: M{excel_row}={r[12]}',f'G2: V{excel_row}={r[21]}',
           f'G6: AI{excel_row}={r[34]}']
    if sid=='RPID_46':
        notes+=['G4: change streams; W/AC/AS extraction fields.',
                'G5: R/AC extraction fields and ECLAIR Section 4, p.426: timestamped models and historical version snapshots; credit for versioning, not zero-downtime adoption.',
                'G7: AO extraction field and ECLAIR Section 3, pp.425-426: manually initiated historical-data backfilling; partial recovery credit, not request continuity.']
    if sid=='RPID_47':
        notes+=['G4: S/AC/AM/AS extraction fields and Axak Section 3.1/Fig.2 describe asynchronous student-behavior events despite W being NR.',
                'G8: AP extraction field and Axak Section 3.1 report Prometheus and ELK.',
                'G7: security/access control is not credited as runtime failure recovery.']
    audit.append(dict(Study_ID=sid,Authors=r[1],Year=r[2],Title=r[3],Workbook_row=excel_row,
                      **{f'G{i+1}':v for i,v in enumerate(scores)},Total=sum(scores),Evidence_notes=' | '.join(notes)))
with (OUT/'SLR_Gap_Coverage_Audit.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(audit[0]));w.writeheader();w.writerows(audit)
stats={'n':len(audit),'total_score':sum(a['Total'] for a in audit),
       'mean':sum(a['Total'] for a in audit)/len(audit),
       'distribution':dict(sorted(collections.Counter(a['Total'] for a in audit).items())),
       'gap_counts':{f'G{i}':dict(collections.Counter(a[f'G{i}'] for a in audit)) for i in range(1,10)}}
(OUT/'SLR_Audit_Summary.json').write_text(json.dumps(stats,indent=2))
print(json.dumps(stats,indent=2))

assert stats["total_score"] == 37.5
assert stats["distribution"] == {0:23,1:17,2:6,4:1,4.5:1}
