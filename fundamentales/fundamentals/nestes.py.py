x = [ [5,2,3], [10,8,9] ] 
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x)
students[0]['first_name']="Braynt"
print(students[0])
sports_directory['soccer'][0]="Andres"
print(sports_directory)
z[0]['y']=30
print(z)
def iterateDictionary(some_list):
    for i in some_list :
        for j in i:
            print(f"{j} - {i[j]} ")
    
iterateDictionary(students)
def iterate_dictionary2(key_name,some_list):
    for i in range(0, len(some_list)):
        
        for key,val in some_list[i].items():
            if key == key_name:
                print(val)
iterate_dictionary2('first_name',students) 


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}]

    
