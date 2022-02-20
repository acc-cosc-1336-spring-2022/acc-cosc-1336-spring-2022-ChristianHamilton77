#create ~f named get_options_ratio that excepts 2 parameters with names option?, Total, -> the ratio

def get_options_ratio(option,total):
    res = option/total
    #print(option/total)
    return res

def get_faculty_rating(res):
    ratio = res

    if ratio >= 0.9 and ratio < 1:
        rating = 'Excellent'
    elif ratio > 0.8:
        rating = 'Very Good'
    elif ratio > 0.7:
        rating = 'Good'
    elif ratio > 0.6 :
        rating = 'Needs Improvement'
    elif ratio > 0 and ratio < 0.6 :
        rating = 'Unacceptable'
    
    return rating 
    #print('The Faculty Rating is', rating)

#create a ~f named get_faculty_rating that accepts the ratio from the get_options_ratio() -> the faculty rating according to the following table
#   //Ratio//           |   //Rating//
#                       |
# >= 0.9 but < 1        | Excellent
# > 0.8                 | Very Good
# > 0.7                 | Good
# > 0.6                 | Needs Improvement
# 0 - 59                | Unacceptable

