def psyic():
    import os
    import time
    print()
    print("This is to test whether you have a Theory of Mind")
    print("You will be shown 5 images which open up independently.")
    print("With each image is shown 2 possible answers.")
    print("The aim is to work out the persons emotion by looking only at the eyes.")
    print("When entering your answer, the spelling has to be exact to provide")
    print("a valid result.")
    print("Heres a test run...")
    input("Press enter when ready...")
    os.system("picture7.jpg")
    print("Playful or serious?")
    testrun = input("> ").lower()
    if testrun == "serious":
        print("Yes, it was a serious message.")
    else:
        print("sorry, it was a serious message.")
    print("Now here comes the real questions...")
    correct = 0
    input("Close the image and press enter for next image...")
    os.system("picture1.jpg")
    print("Sad thought or happy thought?")
    answer1 = input("> ").lower()
    if answer1 == "sad thought":
        correct+=1
    input("Close the image and press enter for next image...")
    os.system("picture2.jpg")
    print("Desire or convinced?")
    answer2 = input("> ").lower()
    if answer2 == "desire":
        correct+=1
    input("Close the image and press enter for next image...")
    os.system("picture3.jpg")
    print("friendly or hostile?")
    answer3 = input("> ").lower()
    if answer3 == "friendly":
        correct+=1
    input("Close the image and press enter for next image...")
    os.system("picture4.jpg")
    print("Making a decision or not making a decision?")
    answer4 = input("> ").lower()
    if answer4 == "making a decision":
        correct+=1
    input("Close the image and press enter for next image...")
    os.system("picture5.jpg")
    print("Noticing or fantasizing?")
    answer5 = input("> ").lower()
    if answer5 == "fantasizing":
        correct+=1
    input("Close the image and press enter for next image...")
    os.system("picture6.jpg")
    print("Calm or anxious?")
    answer6 = input("> ").lower()
    if answer6 == "calm":
        correct+=1
    print("Close the image then your done!")
    print("After you press enter, the results will appear.")
    input("Press enter when ready...")
    print()
    print("Here are the results:")
    print()
    outcome = ("Answer 1 = ",answer1,", answer 2 = ",answer2,", answer 3 = ",answer3,", answer 4 = ",answer4,", answer 5 = ",answer5,", answer 6 = ",answer6)
    testrun2 = (" Test run = ",testrun)
    myfile = open("results.txt","w")
    print()
    if correct > 3:
        print("according to the results, you:")
        print()
        print("have a 'theory of mind'")
        print()
        print("This means, the chances are,")
        print("you don't have autism or asperger syndrome")
        result1 = ("Have a theory of mind ")
        myfile.writelines(result1)
    elif correct <= 3:
        print("according to the results, you:")
        print()
        print("don't have a 'theory of mind'.")
        print()
        print("This means you probably have autism or asperger sydrome.")
        result2 = ("Don't have a theory of mind ")
        myfile.writelines(result2)
    myfile.writelines(outcome)
    myfile.writelines(testrun2)
    myfile.close()
    print()
    print("This test is based on Baron-Cohen's study on Autism Syndrome.")
    print("You should not take this test seriously in anyway due to the")
    print("fact it only contains a part of his study and won't provide")
    print("accurate results.")
    time.sleep(4)
    print()
    print("Thank you for participating.")
    print("A file has been created in the same location as this program.")
    print()
    print("Please send to luke Spanner at lukespanner@btinternet.com.")
    print("Type 'Y' to restart the program otherwise type 'N' to quit.")
    replay = input("Y/N > ").lower()
    if replay == "y":
        psyic()
    else:
        quit()
psyic()
