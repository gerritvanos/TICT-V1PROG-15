def inBoth(lijst1,lijst2):
        gevonden = False
        for index1 in range(0, len(lijst1)):
            for index2 in range(0, len(lijst2)):
                if lijst1[index1] == lijst2[index2]:
                    gevonden = True
                    break
        return (gevonden)


print(inBoth([1,2,3,4,5],[2,7,8,9,6]))