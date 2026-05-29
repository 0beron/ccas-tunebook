import os

tmpl = open("template.txt", "r")

output = open("folder2.tex", "w")

instruments = ['top-horns',
               'bass-horns',
               'soprano-saxophone',
               'tenor-saxophone',
               'tenor-saxophone-1',
               'tenor-saxophone-2',
               'trumpet-in-bb',
               'trombone',
               'tuba',
               'melody',
               'top-horns-liz',
               'top-horns-robin']

def write_template(output, templ):
    abcs = {}
    for abc in os.listdir("abc"):
        for inst in instruments:
            nm, ext = os.path.splitext(abc)
            if nm.endswith(inst):
                bits = nm.split(inst)
                print(bits)


    setlist = []
    st = []
    for line in templ:
        if "subsection" in line:
            setlist.append([line, st])
        if "abcinput" in line:
            st.append(line)
        if "clearpage" in line:
            st = []

    print(setlist)

    for inst in instruments:
        output.write(f"\\section{{{inst}}}\n\n")
        for entry in setlist:
            settns = []
            for tune in entry[1]:
                t2 = tune.split("abc/")[1].split("}")[0]
                t3 = f"{t2}-{inst}"
                tabc = f"{t2}-{inst}.abc"
                if tabc in allabcs:
                    settns.append(f"\\abcinput{{abc/{t3}}}\n")
                    allabcs.remove(tabc)
            print(entry[0])
            print(settns)
            print(" ")

            if len(settns) > 0:
                output.write(entry[0].replace("}", f" ({inst})}}"))
                for t in settns:
                    output.write(t)
                output.write("\\clearpage\n\n")

                
allabcs = os.listdir("abc")

seentempl = False
seenliz = False
templ = []
for line in tmpl:
    if "TEMPLATE" in line:
        seentempl = True

    if "Liz" in line and not seenliz:
        write_template(output, templ)
        seenliz = True

    if not (seentempl or seenliz):
        output.write(line)
    elif seenliz:
        output.write(line)
    else:
        templ.append(line)



            
        
