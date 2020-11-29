number = 1000
n=number
path1 = "ref.fasta"
pathX = "sample_2.fastq"
pathC = "mapping_ground_truth.txt"
import main

def run():
    print("lets rumblee")
    import time
    t = time.time()
    main.runengine(number, path1, pathX)
    time = time.time()-t

    import certifier
    certifier.get_firstx_reads(number, pathC)
    accuracy, precision = certifier.certify()

    print("Accuracy: ", accuracy)
    print("Precision: ", precision)
    print(str(n*1.*60./time) + "reads per min")

run()
