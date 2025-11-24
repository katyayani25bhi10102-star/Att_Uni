print("=============== University Attendance Calculator ===============\n")

num_sub= int(input("Enter number of subjects: "))

sub = {}
t_attended = 0
t_classes = 0

for i in range(num_sub):
    print(f"\nSubject {i+1}:")
    sub_name = input("Subject name: ")

    held = int(input("Total classes held: "))
    attended = int(input("Classes attended: "))

    percent = (attended / held) * 100
    sub[sub_name] = percent

    t_attended += attended
    t_classes += held

print("\n========== Attendance Report ==========\n")
for s, p in sub.items():
    print(f"{s}: {p:.2f}%")

overall = (t_attended / t_classes) * 100
print("\nOverall Attendance:", f"{overall:.2f}%")

if overall < 75:
    print("\nWarning: Attendance is below 75%!")
else:
    print("\nAttendance is sufficient.")