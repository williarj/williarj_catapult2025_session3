import random
seq1 = "ATTG"
seq2 = "CGCA"
seq3 = "GGGC"

counselors = ["Alex", "Eathan", "Dustee", "Emre", "Anthony", "Mary",
              "Akshad", "Lorelai", "Michael", "Mikey", "Michael (again)",
              "Emmet", "Molly", "Jeffrey", "Faith", "Winston"]

def generateSTRseq(n):
    #sequencies vary by about 10% in length
    n = n + random.randint(0, n*0.1)
    seq = ""
    while len(seq) < n:
        seq += seq1
        if(random.random() < 0.1):
            break
    while len(seq) < n:
        seq += seq2
        if(random.random() < 0.2):
            break
    while (len(seq) < n):
        seq += seq3
    return seq

length = 200

seqs = {}

for c in counselors:
    print(">"+c)
    seq = generateSTRseq(length)
    seqs[c] = seq
    print(seq)

print(">culprit")
print(random.choice(list(seqs.values())))


