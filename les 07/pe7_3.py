cijfers = {'gerrit':9,'maarten':8,'maikel':7,'enno':6,'sander':6,'stef':8,'eric':9,'ethem':10}

for student in cijfers:
    if cijfers[student]>=9:
        print('{} heeft een {}'.format(student,cijfers[student]))