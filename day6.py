paltan = ["Karan", "Commando", "Sher", "Tiger", "Baaz"]

print("Meri GHATAK Paltan:")
print(paltan)

print("\nPehla Commando:", paltan[0])
print("Aakhri Commando:", paltan[4])
print("Total Jawans:", len(paltan))

print("\n--- Full Roll Call ---")
for jawan in paltan:
    print("Jai Hind", jawan)

# EXTRA GHATAK TASK
paltan.append("Cheeta")
print("\nNaya Jawan add hua:", paltan)
