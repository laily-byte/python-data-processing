import pandas as pd
fname = input("Enter file name: ")
fn = pd.read_csv(fname, sep = ";", decimal=",")

fn.columns = [
    'name',
    'semester_1',
    'semester_2',
    'summer_exam',
    'diploma'
]
fn_students = fn[fn['name'] != 'Maximum Value']

print(fn)
fnss1 = fn_students['semester_1'] != 0
as1 = round(fn_students['semester_1'][fnss1].mean(), 2)
fnss2 = fn_students['semester_2'] != 0
as2 = round(fn_students['semester_1'][fnss2].mean(), 2)
fnsse = fn_students['summer_exam'] != 0
ase = round(fn_students['semester_1'][fnsse].mean(), 2)
fnsd = fn_students['diploma'] != 0
ad = round(fn_students['diploma'][fnsd].mean(), 2)
print("Total Students:", len(fn_students))

print("Average Grade in First Semester:", as1)
print("Average Grade in Second Semester:", as2)
print("Average Grade in Summer Exam:", ase)
print("Average Diploma:", ad)

print(
    "Highest Grade in First Semester:", 
    fn_students['semester_1'].max(), 
    ":", 
    ", ".join(
    fn_students.loc[
        fn_students['semester_1'] == fn_students['semester_1'].max(), 
        'name'
        ].tolist()
    )
)

print(
    "Highest Grade in Second Semester:", 
    fn_students['semester_2'].max(), 
    ":", 
    ", ".join(
    fn_students.loc[
        fn_students['semester_2'] == fn_students['semester_2'].max(), 
        'name'
        ].tolist()
    )
)

print(
    "Highest Grade in Summer Exam:", 
    fn_students['summer_exam'].max(), 
    ":", 
    ", ".join(
    fn_students.loc[
        fn_students['summer_exam'] == fn_students['summer_exam'].max(), 
        'name'
        ].tolist()
    )
)

print(
    "Highest Grade in Diploma:", 
    fn_students['diploma'].max(), 
    ":", 
    ", ".join(
    fn_students.loc[
        fn_students['diploma'] == fn_students['diploma'].max(), 
        'name'
        ].tolist()
    )
)
