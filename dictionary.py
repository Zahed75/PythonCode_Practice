#dictionary key er moddhe value store kore rakhe ja colon diye korte hoy
student_id={
    "101" : "Zahed Hasan",
    "102" : "Taniya Akhter",
    "103" : "Saima Islam",
}
print(student_id)
print(student_id["102"])
#get fun when none exits key in this list
print(student_id.get("103","Not a vlaid key found"))#get ja pabe tai e dekhabe