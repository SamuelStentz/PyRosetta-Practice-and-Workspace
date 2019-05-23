from pyrosetta import *
init()
p = pose_from_file("1UBQ.pdb.gz")
sfxn = get_score_function()
print("Here I am!")
print("\n\n\n")
print(sfxn(p))
