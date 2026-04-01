student_data={
    "id1":{"name":"John","Class":5, "Subject_Interrogation":"Maths,Science"},
    "id2":{"name":"Emma","Class":5, "Subject_Interrogation":"Maths,Science"},
    "id3":{"name":"John","Class":5, "Subject_Interrogation":"Maths,Science"},
    "id4":{"name":"Olivia","Class":5, "Subject_Interrogation":"Maths,Science"}
}
result={}
seen_Keys=[]
for student_id, details in student_data.items():
    unique_key = details["name"],details["Class"],
    details["Subject_Interrogation"]
    if unique_key not in seen_Keys:
      seen_Keys.append(unique_key)
      result[student_id] = details
for k,v in result.items():
 print(k,":",v)
    