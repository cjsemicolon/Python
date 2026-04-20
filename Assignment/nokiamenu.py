print("List of menu functions \n1.  Phone book\n2.  Messages\n3.  Chat\n4.  Call register\n5.  Tones\n6.  Settings\n7.  Call divert\n8.  Games\n9.  Calculator\n10. Reminders\n11. Clock\n12. Profiles\n13. SIM services")

main_menu_choice = int(input("Select\n"))

match main_menu_choice:

    case 1:
        print("Phone book\n1. Search\n2. Service Nos\n3. Add name\n4. Erase\n5. Edit\n6. Assign Tone\n7. Send b'card\n8. Options\n9. Speed dials\n10. Voice tags")

        phone_book_choice = int(input("Select\n"))

        match phone_book_choice:

            case 1:
                print("Search")

            case 2:
                print("Service Nos")

            case 3:
                print("Add name")

            case 4:
                print("Erase")

            case 5:
                print("Edit")

            case 6:
                print("Assign Tone")

            case 7:
                print("Send b'card")

            case 8:
                print("Options\n1. Type of view\n2. Memory status")
                options_choice = int(input("Select\n"))

                match options_choice:
                    case 1:
                        print("Type of view")

                    case 2:
                        print("Memory status")

                    case _:
                        print("invalid choice")

            case 9:
                print("Speed dials")

            case 10:
                print("Voice tags")

            case _:
                print("invalid choice")
    case 2:
        print("Messages\n1. Write messages\n2. Inbox\n3. Outbox\n4. Picture messages\n5. Templates\n6. Smileys\n7. Message settings\n8. Info service\n9. Voice mailbox number\n10. Service command editor")

        messages_choice = int(input("Select\n"))

        match messages_choice:

            case 1:
                print("Write messages")

            case 2:
                print("Inbox")

            case 3:
                print("Outbox")

            case 4:
                print("Picture messages")

            case 5:
                print("Templates")

            case 6:
                print("Smileys")

            case 7:
                print("Message settings\n1. Set\n2. Common")

                message_settings_choice = int(input("Select\n"))

                match message_settings_choice:

                    case 1:
                        print("Set\n1. Message center number\n2. Message sent as\n3. Message validity")

                        set_choice = int(input("Select\n"))

                        match set_choice:

                            case 1:
                                print("Message center number")

                            case 2:
                                print("Message sent as")

                            case 3:
                                print("Message validity")

                            case _:
                                print("Invalid choice")

                    case 2:
                        print("Common\n1. Delivery reports\n2. Reply via same center\n3. Character support")

                        common_choice = int(input("Select\n"))

                        match common_choice:

                            case 1:
                                print("Delivery reports")

                            case 2:
                                print("Reply via same center")

                            case 3:
                                print("Character support")

                            case _:
                                print("Invalid choice")

            case 8:
                print("Info service")

            case 9:
                print("Voice mailbox number")

            case 10:
                print("Service command editor")

            case _:
                print("Invalid choice")

    case 3:
        print("Chat")

    case 4:
        print("Call register\n1. Missed calls\n2. Received calls\n3. Dialled numbers\n4. Erase recent call list\n5. Show call duration\n6. Show call costs\n7. Call cost settings\n8. Prepaid credit")

        call_register = int(input("Select\n"))

        match call_register:

            case 1:
                print("Missed calls")

            case 2:
                print("Received calls")

            case 3:
                print("Dialled numbers")

            case 4:
                print("Erase recent call list")

            case 5:
                print("Show call duration\n1. Last call duration\n2. All calls duration\n3. Received calls duration\n4. Dialled calls duration\n5. Clear timers")

                call_duration_choice = int(input("Select\n"))

                match call_duration_choice:

                    case 1:
                        print("Last call duration")

                    case 2:
                        print("All calls duration")

                    case 3:
                        print("Received calls duration")

                    case 4:
                        print("Dialled calls duration")

                    case 5:
                        print("Clear timers")

                    case _:
                        print("Invalid choice")

            case 6:
                print("Show call costs\n1. Last call cost\n2. All calls cost\n3. Clear counters")

                show_call_costs_choice = int(input("Select\n"))

                match show_call_costs_choice:

                    case 1:
                        print("Last call cost")

                    case 2:
                        print("All calls cost")

                    case 3:
                        print("Clear counters")

            case 7:
                print("Call cost settings\n1. Call cost limit\n2. Show cost in")

                call_cost_settings = int(input("Select\n"))

                match call_cost_settings:

                    case 1:
                        print("Call cost limit")

                    case 2:
                        print("Show cost in")

                    case _:
                        print("Invalid choice")

            case 8:
                print("Prepaid credit")

            case _:
                print("Invalid choice")

    case 5:
        print("Tones\n1. Ringing tone\n2. Ringing volume\n3. Incoming call alert\n4. Composer\n5. Message alert tone\n6. Keypad tones\n7. Warning and game tones\n8. Vibrating alert\n9. Screen saver")

        tones_choice = int(input("Select\n"))

        match tones_choice:

            case 1:
                print("Ringing tone")

            case 2:
                print("Ringing volume")

            case 3:
                print("Incoming call alert")

            case 4:
                print("Composer")

            case 5:
                print("Message alert tone")

            case 6:
                print("Keypad tones")

            case 7:
                print("Warning and game tones")

            case 8:
                print("Vibrating alert")

            case 9:
                print("Screen saver")

            case _:
                print("Invalid choice")

    case 6:
        print("Settings\n1. Call settings \n2. Phone settings\n3. Security settings\n4. Restore factory settings")

        settings_choice = int(input("Select\n"))

        match settings_choice:

            case 1:
                print("Call settings\n1. Automatic redial\n2. Speed dialling\n3. Call waiting options\n4. Own number sending\n5. Phone line in use\n6. Automatic answer")

                call_setting = int(input("Select\n"))

                match call_setting:

                    case 1:
                        print("Automatic redial")

                    case 2:
                        print("Speed dialling")

                    case 3:
                        print("Call waiting options")

                    case 4:
                        print("Own number sending")

                    case 5:
                        print("Phone line in use")

                    case 6:
                        print("Automatic answer")

                    case _:
                        print("Invalid choice")

            case 2:
                print("Phone settings\n1. Language\n2. Cell info display\n3. Call waiting options\n4. Welcome note\n5. Lights\n6. Confirm SIM service actions")

                phone_setting = int(input("Select\n"))

                match phone_setting:

                    case 1:
                        print("Language")

                    case 2:
                        print("Cell info display")

                    case 3:
                        print("Call waiting options")

                    case 4:
                        print("Welcome note")

                    case 5:
                        print("Lights")

                    case 6:
                        print("Confirm SIM service actions")

                    case _:
                        print("Invalid choice")

            case 3:
                print("Security settings\n1. PIN code request\n2. Call barring service\n3. Fixed dialling\n4. Closed user group\n5. Phone security\n6. Change access codes")

                security_setting = int(input("Select\n"))

                match security_setting:

                    case 1:
                        print("PIN code request")

                    case 2:
                        print("Call barring service")

                    case 3:
                        print("Fixed dialling")

                    case 4:
                        print("Closed user group")

                    case 5:
                        print("Phone security")

                    case 6:
                        print("Change access codes")

                    case _:
                        print("Invalid choice")

            case 4:
                print("Restore factory settings")

    case 7:
        print("Call divert")

    case 8:
        print("Games")

    case 9:
        print("Calculator")

    case 10:
        print("Reminders")

    case 11:
        print("Clock\n1. Alarm clock\n2. Clock settings\n3. Date setting\n4. Stopwatch\n5. Countdown timer\n6. Auto update of date and time")

        clock_choice = int(input("Select\n"))

        match clock_choice:

            case 1:
                print("Alarm clock")

            case 2:
                print("Clock settings")

            case 3:
                print("Date setting")

            case 4:
                print("Stopwatch")

            case 5:
                print("Countdown timer")

            case 6:
                print("Auto update of date and time")

            case _:
                print("Invalid choice")

    case 12:
        print("Profiles")

    case 13:
        print("SIM services")

    case _:
        print("Invalid choice")
