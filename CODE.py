while True:
    print("\n===== Straight Line Calculator =====")
    print("1. Chapter Overview")
    print("2. Important Formulas")
    print("3. Solve a Problem")
    print("4. Exit")
    
    try:
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1:
            print("""
            The Straight Line chapter covers:
            - Slope of a line
            - Different forms of a line equation (Slope-Intercept, Point-Slope, Two-Point, Intercept Form)
            - Angle between two lines
            - Parallel & Perpendicular conditions
            - Distance of a point from a line
            - Midpoint and Section formula
            """)
        
        elif choice == 2:
            print("""
            Important Formulas:
            1. Slope: m = (y2 - y1) / (x2 - x1)
            2. Slope-Intercept Form: y = mx + c
            3. Point-Slope Form: y - y1 = m(x - x1)
            4. Two-Point Form: (y - y1) = ((y2 - y1) / (x2 - x1)) * (x - x1)
            5. Intercept Form: (x/a) + (y/b) = 1
            6. Angle Between Two Lines: tanθ = |(m2 - m1) / (1 + m1 * m2)|
            7. Distance of Point (x1, y1) from Line Ax + By + C = 0:
               Distance = |Ax1 + By1 + C| / sqrt(A^2 + B^2)
            8. Midpoint Formula: ((x1 + x2)/2 , (y1 + y2)/2)
            9. Section Formula: ((mx2 + nx1)/(m+n) , (my2 + ny1)/(m+n))
            """)
        
        elif choice == 3:
            print("\nSelect a problem type:")
            print("1. Find the Slope of a Line")
            print("2. Find the Equation of a Line")
            print("3. Find the Distance of a Point from a Line")
            print("4. Find the Angle Between Two Lines")
            print("5. Find the Intersection of Two Lines")
            problem_choice = int(input("Enter your choice (1-5): "))

            if problem_choice == 1:
                x1, y1 = map(float, input("Enter x1 and y1: ").split())
                x2, y2 = map(float, input("Enter x2 and y2: ").split())
                if x2 - x1 != 0:
                    slope = (y2 - y1) / (x2 - x1)
                    print(f"Slope: {slope}")
                else:
                    print("The line is vertical; slope is undefined.")

            elif problem_choice == 2:
                print("\nChoose the equation form:")
                print("1. Slope-Intercept Form")
                print("2. Point-Slope Form")
                form_choice = int(input("Enter your choice (1-2): "))
                
                if form_choice == 1:
                    m = float(input("Enter slope (m): "))
                    c = float(input("Enter y-intercept (c): "))
                    print(f"Equation: y = {m}x + {c}")
                
                elif form_choice == 2:
                    x1, y1 = map(float, input("Enter x1 and y1: ").split())
                    m = float(input("Enter slope (m): "))
                    print(f"Equation: y - {y1} = {m}(x - {x1})")

            elif problem_choice == 3:
                A, B, C = map(float, input("Enter coefficients A, B, and C of the line Ax + By + C = 0: ").split())
                x1, y1 = map(float, input("Enter x and y of the point: ").split())
                distance = abs(A * x1 + B * y1 + C) / ((A**2 + B**2) ** 0.5)
                print(f"Distance: {distance}")
            
            elif problem_choice == 4:
                m1 = float(input("Enter slope of first line (m1): "))
                m2 = float(input("Enter slope of second line (m2): "))
                from math import atan, degrees
                angle = abs(degrees(atan((m2 - m1) / (1 + m1 * m2))))
                print(f"Angle between lines: {angle} degrees")
            
            elif problem_choice == 5:
                a1, b1, c1 = map(float, input("Enter coefficients (A1, B1, C1) for first line: ").split())
                a2, b2, c2 = map(float, input("Enter coefficients (A2, B2, C2) for second line: ").split())
                determinant = a1 * b2 - a2 * b1
                if determinant == 0:
                    print("Lines are parallel or coincident; no intersection.")
                else:
                    x = (b2 * (-c1) - b1 * (-c2)) / determinant
                    y = (a1 * (-c2) - a2 * (-c1)) / determinant
                    print(f"Intersection point: ({x}, {y})")
            
            else:
                print("Invalid choice! Please enter a valid option.")
        
        elif choice == 4:
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")
    
    except ValueError:
        print("Invalid input! Please enter a number.")
