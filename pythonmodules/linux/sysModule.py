import sys
ur_srt=sys.argv[1]
in_act=sys.argv[2]

if ur_srt=="lower":
    print(ur_srt.lower())
elif ur_srt=="upper":
    print(ur_srt.upper())
elif ur_srt=="title":
    print(ur_srt.title())
else:
    print("Your have printed invalit option...")


