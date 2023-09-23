def isValid(s):
        char1="()"
        char2="{}"
        char3="[]"
        if (char1[0] and char1[1]) in s:
            return "true"
        elif (char2[0] and char2[1]) in s:
            return "true"
        elif  (char3[0] and char3[1]) in s:
            return "true"
        else:
            return "false"
