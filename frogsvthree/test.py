from frogpackage import dbmgmt, names_list
import random

gender = ["Male", "Female"]
environment = ["Dry", "Humid"]
copulation = ["Y", "N"]

dbmgmt.create_table()
dbmgmt.create_tadpole_table()

condition = input("Welcome to Frog Life! What would you like to do today? Type 'help' to get a list of commands.\n")

while condition != "exit":

    pond_env = random.choice(environment)

    print("Today's weather at the pond is... " + pond_env)

    # You can choose to populate the frog table here...
    if condition == "add":
        quantity = input("How many frogs would you like in the pond?\n")
        [dbmgmt.dynamic_data_entry(random.choice(gender), copulation) for x in range(int(quantity))]

    # Display all the records in the Frog table...
    elif condition == "display":
        dbmgmt.read_from_table()

    # Delete all records from the Frog table...
    elif condition == "delete all":
        dbmgmt.delete_all()

    # Feed the frogs to keep them from dying...
    elif condition == "feed":
        print("Frogs have been fed!\n+" + str(dbmgmt.update_plus_lifecycles()) + " lives!")

    # Search for specific Frog in the table...
    elif condition == "search":
        criterion = input("Type 'name', 'gender', 'lifecycles' or 'mating' followed by a space and the criterion to"
                          " search by to display specified frogs...\n")
        if "name" in criterion:
            dbmgmt.read_by_name(criterion.split()[1])
        elif "gender" in criterion:
            dbmgmt.read_by_gender(criterion.split()[1])
        elif "lifecycles" in criterion:
            dbmgmt.read_by_lifecycles(criterion.split()[1])
        elif "mating" in criterion:
            dbmgmt.read_by_copulation(criterion.split()[1])

    # Display all the records in the Tadpole table...
    elif "display tadpoles" in condition:
        dbmgmt.read_from_tadpole_table()

    # Display the list of commands that can be input...
    elif condition == "help":
        print("List of commands:\n" + "display\n" + "add\n" + "delete all\n" + "feed\n" + "search\n" +
              "display tadpoles\n" + "exit")

    # Deciding the pond's environment...
    if pond_env == "Dry":
        dbmgmt.update_minus_lifecycles()

    # Chooses two random male and female frogs to mate...
    if dbmgmt.check_rows_exist() is True:
        male_mate = dbmgmt.select_male_frog_mate()
        female_mate = dbmgmt.select_female_frog_mate()

        let_mate = input(male_mate[1] + " and " + female_mate[1] + " seems to like each other... Mate? (Y/N)\n")
        if let_mate == "Y":
            print(male_mate[1] + " and " + female_mate[1] + " have mated!")
            [dbmgmt.dynamic_data_entry_tadpole(random.choice(gender), male_mate[1], female_mate[1]) for x in
             range(random.randrange(10, 20))]
            print("Tadpoles are in the pond now!")
        else:
            print(male_mate[1] + " and " + female_mate[1] + " did not mate...")

    # Get rid of dead frogs from the table...
    dbmgmt.delete_dead_frogs()

    dbmgmt.close_db()

    condition = input("What's next?\n")
