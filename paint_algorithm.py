def paint_algorithm(number_of_rooms_to_paint, per_gallon_price, wall_space_in_square_feet):
    # print total number of rooms to paint
    print(f"Total number of rooms to paint are: {number_of_rooms_to_paint}")

    # return the number of gallons of paint required
    num_of_gallons = wall_space_in_square_feet // 115
    print(f"Number of gallons of paint required are: {num_of_gallons}")

    # return the hours of labor required
    total_labor_hours = (wall_space_in_square_feet // 115) * 8
    print(f"Total hours of labor is: {total_labor_hours} Hours")

    # return the cost of paint
    total_paint_cost = (wall_space_in_square_feet / 115) * per_gallon_price
    print(f"Total paint cost is: ${total_paint_cost}")

    # return the labor charges 
    labor_charges = ((wall_space_in_square_feet / 115) * 8) * 18
    print(f"Labor charges are: ${labor_charges}")

    # return total cost of the paint
    total_paint_job_cost = total_labor_hours + total_paint_cost + labor_charges
    print(f"Total cost of the paint job is: ${total_paint_job_cost}")


number_of_rooms_to_paint = int(input("Enter the number of rooms to paint: "))
per_gallon_price = int(input("Enter the price of the paint per gallon: "))
wall_space_in_square_feet = int(input("Enter the wall space of each room in SQUARE FEET: "))

paint_algorithm(number_of_rooms_to_paint, per_gallon_price, wall_space_in_square_feet)
