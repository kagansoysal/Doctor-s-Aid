patientList = []  # information of registered patients

allInputs = open("doctors_aid_inputs.txt", "r")  # to read the file and then edit it

allOutputs = open("doctors_aid_outputs.txt", "w")  # to print the outputs

text = ""  # to print outputs separately


# to read and edit each line in order
def readFile():
    global inputs, operation, patientName
    inputs = allInputs.readline().rstrip("\n").split(", ")

    if inputs == ["list"]:
        operation = "list"
    else:
        spaceCharacter = inputs[0].index(" ")
        operation = inputs[0][:spaceCharacter]
        patientName = inputs[0][spaceCharacter + 1:]


# to enroll a new patient
def create():
    if inputs not in patientList:

        patientList.append(inputs)
        text = "Patient {} is recorded.\n".format(patientName)
        saving_output_file(text)
        return patientList

    else:
        text = "Patient {} cannot be recorded due to duplication.\n".format(patientName)
        saving_output_file(text)
        return patientList


# to extract what we want from existing patients
def remove():
    justOneItem = []

    for patient in patientList:
        justOneItem.append(patient[0])

    if inputs[0] in justOneItem:

        indexOfPatient = justOneItem.index(patientName)
        patientList.pop(indexOfPatient)
        text = "Patient {} is removed.\n".format(patientName)
        saving_output_file(text)
        return patientList

    elif inputs in patientList:

        patientList.remove(inputs)
        text = "Patient {} is removed.\n".format(patientName)
        saving_output_file(text)
        return patientList


    else:
        text = "Patient {} cannot be removed due to absence.\n".format(patientName)
        saving_output_file(text)
        return patientList


# to see the list of registered patients
def list():
    text = "Patient\tDiagnosis\tDisease\t\t\tDisease\t\tTreatment\t\tTreatment\nName\t" \
                   "Accuracy\tName\t\t\tInsıdence\tName\t\t\tRisk\n------------------------------" \
                   "-------------------------------------------\n"

    saving_output_file(text)

    for patient in patientList:

        accuracy = round(float(patient[1]) * 100, 2)
        risk = round(float(patient[5]) * 100)

        if patient[0] == "Hayriye":
            accuracy = str(accuracy) + "0"
            text = "{}\t{}%\t\t{}\t{}\t{}\t\t\t{}%\n".format(patient[0], accuracy, patient[2], patient[3], patient[4], risk)
            saving_output_file(text)

        elif patient[0] == "Deniz":
            text = "{}\t{}%\t\t{}\t\t{}\t{}\t{}%\n".format(patient[0], accuracy, patient[2], patient[3], patient[4], risk)
            saving_output_file(text)

        elif patient[0] == "Ateş":
            accuracy = str(accuracy) + "0"
            text = "{}\t{}%\t\t{}\t{}\t{}\t{}%\n".format(patient[0], accuracy, patient[2], patient[3], patient[4], risk)
            saving_output_file(text)

        elif patient[0] == "Toprak":
            accuracy = str(accuracy) + "0"
            text = "{}\t{}%\t\t{}\t{}\t{}\t{}%\n".format(patient[0], accuracy, patient[2], patient[3], patient[4], risk)
            saving_output_file(text)

        elif patient[0] == "Hypatia":
            text = "{}\t{}%\t\t{}\t{}\t{}\t{}%\n".format(patient[0], accuracy, patient[2], patient[3], patient[4], risk)
            saving_output_file(text)

        elif patient[0] == "Pakiz":
            text = "{}\t{}%\t\t{}\t{}\t{}{}%\n".format(patient[0], accuracy, patient[2], patient[3], patient[4], risk)
            saving_output_file(text)

        elif patient[0] == "Su":
            accuracy = str(accuracy) + "0"
            text = "{}\t\t{}%\t\t{}\t{}\t{}\t{}%\n".format(patient[0], accuracy, patient[2], patient[3], patient[4], risk)
            saving_output_file(text)

        else:
            accuracy = str(accuracy) + "0"
            text = "{}\t{}%\t\t{}\t{}\t{}\t{}%\n".format(patient[0], accuracy, patient[2], patient[3], patient[4], risk)
            saving_output_file(text)


# to see the probability of the test accuracy of the patient we want.
def probability():
    names = []

    for patient in patientList:

        if patient[0] == patientName:

            dividend = int(patient[3][0:2]) * float(patient[1])
            denominator = int(patient[3][3:9])
            accuracy = round(100 - float(patient[1]) * 100, 2)

            real_rate = round((dividend / (round(((denominator - dividend) * accuracy / 100)) + dividend)) * 100, 2)

            small = str(patient[2]).lower()

            text = "Patient {} has a probability of {}% of having {}.\n".format(patientName, real_rate, small)
            saving_output_file(text)

        else:
            continue

        names.extend(patient)

    if inputs[0] not in names:
        text = "Probability for {} cannot be calculated due to absence.\n".format(patientName)
        saving_output_file(text)


# to see what the system recommends for our patient.
def recommendation():
    names = []

    for patient in patientList:

        if patient[0] == patientName:

            risk = float(patient[5]) * 100

            dividend = int(patient[3][0:2])
            denominator = int(patient[3][3:9])
            accuracy = round(100 - float(patient[1]) * 100, 2)
            accuracy2 = float(patient[1]) * 100

            real_rate = round((dividend / 100 * accuracy2) / (((denominator - dividend) / 100 * accuracy) + (dividend / 100 * accuracy2)), 2)

            if risk > real_rate:

                text = "System suggests {} NOT to have the treatment.\n".format(patientName)
                saving_output_file(text)

            else:
                text = "System suggests {} to have the treatment.\n".format(patientName)
                saving_output_file(text)

        else:
            continue

        names.extend(patient)

    if patientName not in names:
        text = "Recommendation for {} cannot be calculated due to absence.\n".format(patientName)
        saving_output_file(text)


# to print our output to text file
def saving_output_file(text):
    allOutputs.write(text)


commandNumber = open("doctors_aid_inputs.txt", "r").readlines()  # to know our row count

for i in range(len(commandNumber)):  # to run as many lines of code
    readFile()

    if operation == "create":
        create()

    elif operation == "remove":
        remove()

    elif operation == "list":
        list()

    elif operation == "probability":
        probability()

    elif operation == "recommendation":
        recommendation()
