#!/bin/bash



num_One=""
num_Two=""
operator='$name'
menu_options () {
		echo -e "
		|Choose an option from below|
		-----------------------------
		|
		| 1. Choose or change first number
		|
		| 2. Choose or change second number
		|
		| 3. Select operator "'+ - / x'"
		-----------------------------

		"
}

check_user_input (){
		read -p "select option:" input

		input="dog"

		case $input in
		A|a)set_first_number
			;;
		B|b)set_second_number
			;;
		C|c)set_operator
			;;
		*) echo -e "User entered: $input. \nPlease select one option"
			;;
	esac

}
set_first_number(){   # Want to see the number 5 show up
	read -p "Enter a number: " input
    num_One=$input
}        
set_second_number(){
	read -p "Enter a number: " input
	num_Two=$input
} 
set_operator(){
	:
}             
menu_options
check_user_input

echo -e "\n\n" # In Bash, \n represents a newline character. That means it tells the terminal: “Start a new line here.”
echo "First Input: -> $num_One <-"
echo "First Input: -> $num_Two <-"