class Math:

    def square(self,number):
        """This function return square of given number"""
        return number*number
    def cube(self,number):
        """This function return cube of given number"""
        return number*number*number
    def ar_sqr(self,number):
        """This function return area of square"""
        return number*number
    def ar_rectangle(self,length,breadth):
        """This function return area of rectangle"""
        return length*breadth
    def cube_root(self,number):
        """This function return cube root of given number"""
        return pow(number,1/3)
    def square_root(self,number):
        """This function return the square root of given number"""
        return pow(number,1/2)
    def ar_triangle(self,height,base):
        """This function return the area of triangle"""
        return 0.5*height*base
    def ar_triangle_Heron(self,side1,side2,side3):
        """This function returns the area of triangle by using Heron's formula"""
        s=(side1+side2+side3)/2
        sq_ar=s*(s-side1)*(s-side2)*(s-side3)
        return pow(sq_ar,1/2)
    def pythogoras(self,hypotenuse,perpendicular,base):
        """This function returns the any one paramater between hypotenuse,base and perpendicular  """
        if base==None:
            return hypotenuse*hypotenuse-perpendicular*perpendicular
        elif perpendicular==None:
            return hypotenuse*hypotenuse-base*base
        elif hypotenuse==None:
            return base*base+perpendicular*perpendicular
        else:
            raise Exception("Invalid input")
    def ar_parallelogram(self,base,height):
        """This function returns the area of parallelogram"""
        return base*height
    def ar_trapezium(self,side1,side2,height):
        """This function returns the area of trapezium"""
        return 0.5*height(side2+side1)
    def quadratic_eqn(self,a,b,c):
        """This function returns the solution of quadratic equation"""
        D=(b*b)-(4*a*c)
        root_D=pow(D,1/2)
        soln_pos=(-b+root_D)/(2*a)
        soln_neg=(-b-root_D)/(2*a)
        return soln_neg,soln_pos
    def AP_term(self,d,a,n):
        """This function returns the value of nth term"""
        return a+((n-1)*d)
    def summation(self,a,n,d):
        """This function returns the summation upto nth term"""
        temp=(2*a)+((n-1)*d)
        return (n/2)*temp
    def factorial(self,number):
        """This function returns the factorial of given number"""
        fac=1
        for i in  range(1,number+1):
            fac=fac*i
        return fac
    def AP(self,n,a,d):
        """This method returns the series upto nth term"""
        temp_list=[a]
        for i in range(1,n):

            term=a+(i*d)
            temp_list.append(term)
        return temp_list
    @staticmethod
    def AP_info(*AP):
        """This method returns the information of AP"""
        AP_list=list(AP)
        return f"a={AP_list[0]},d={AP_list[1]-AP_list[0]} and n={len(AP_list)}"
    def fibonacci_sequence(self,n):
        """This method returns fibonacci sequence upto nth term"""
        temp_list=[0,1]
        for i in range(1,n-1):
            temp=temp_list[i]+temp_list[i-1]
            temp_list.append(temp)
        return temp_list
    def fibonacci_term(self,n):
        """This method returns the nth terms of fibonacci sequence"""
        temp_list = [0, 1]
        for i in range(1, n - 1):
            temp = temp_list[i] + temp_list[i - 1]
            temp_list.append(temp)
        return temp_list[n-1]
    def pair_linear_equn(self,a1,b1,c1,a2,b2,c2):
        """This method returns the solution of a pair of linear equation"""
        if (a1/a2)!=(b1/b2)!=(c1/c2):#unique solution
            x=((b1*c2)-(b2*c1))/((a1*b2)-(a2*b1))
            y=((c1*a2)-(c2*a1))/((a1*b2)-(a2*b1))
            return f"x={x},y={y}"
        elif (a1/a1)==(b1/b2)==(c1/c2):#infinitely solution
            return f"Infinitely many solution"
        else:
            return f"No solution"
    def system_linear_equn(self,a1,b1,c1,a2,b2,c2):
        """This method returns the type of solution of a pair of linear equation"""
        if (a1 / a2) != (b1 / b2) != (c1 / c2):  # unique solution

            return f"Unique solution"
        elif (a1 / a1) == (b1 / b2) == (c1 / c2):  # infinitely solution
            return f"Infinitely many solution"
        else:
            return f"No solution"
    def golden_ratio(self):
        """This method returns the value of golden ratio"""
        temp=1.61803398875
        return temp
    def TSA_cuboid(self,l,b,h):
        """This method returns the TSA of cuboid"""
        return 2*((l*b)+(b*h)+(h*l))
    def TSA_cube(self,a):
        """This method returns the TSA of cube"""
        return 6*(a*a)
    def TSA_cylinder(self,r,h):
        """This method returns the TSA of cylinder"""
        return (2*3.14*r)*(r+h)
    def CSA_cone(self,r,l,h):
        """This method return the CSA of right circular cone"""
        if l==None:
            temp=(r*r)+(h*h)
            l=pow(temp,1/2)
            return (3.14*r*l)
        elif h==None:
            return (3.14*r*l)
        else:
            raise Exception("Invalid input")
    def SA_sphere(self,r):
        """This method returns the SA of sphere"""
        return (4*3.14*r*r)
    def TSA_hemisphere(self,r):
        """This method returns the TSA of hemisphere"""
        return (3*3.14*r*r)
    def CSA_cuboid(self,l,b,h):
        """This method returns the CSA of cuboid"""
        return (2*(l+b)*h)
    def CSA_cube(self,a):
        """This method returns the CSA of cube"""
        return (4*a*a)
    def CSA_cylinder(self,r,h):
        """This method returns the CSA of cylinder"""
        return (2*3.14*r*h)

    def TSA_cone(self, r, l, h):
        """This method return the TSA of right circular cone"""
        if l == None:
            temp = (r * r) + (h * h)
            l = pow(temp, 1 / 2)
            return (3.14 * r)*( r+l)
        elif h == None:
            return (3.14 * r)*(r * l)
        else:
            raise Exception("Invalid input")

    def  CSA_hemisphere(self,r):

        """This method returns the CSA of hemisphere"""
        return (2*3.14*r*r)
    def volume_cuboid(self,l,b,h):
        """This method returns the volume of cuboid"""
        return (l*b*h)
    def volume_cube(self,a):
        """This method returns the volume of cube"""
        return (a*a*a)
    def volume_cylinder(self,r,h):
        """This method returns the volume of cylinder"""
        return (3.14*r*r*h)
    def volume_cone(self,r,h,l):
        """This method returns the volume of cone"""

        if l == None:
            temp = (r * r) + (h * h)
            l = pow(temp, 1 / 2)
            return (1/3)*(3.14*r*r*h)
        elif h == None:
            return (1/3)*(3.14*r*r*h)
        else:
            raise Exception("Invalid input")

    def volume_sphere(self,r):
        """This method returns the volume of sphere"""
        return (4/3)*(3.14*r*r*r)
    def volume_hemisphere(self,r):
        """This method returns the volume of hemisphere"""
        return (2/3)*(3.14*r*r*r)
    def CSA_frustum_cone(self,R,r,l,h):
        """This method returns the CSA of frustum of cone"""
        if l == None:
            temp = ((h*h)+((R-r)*(R-r)))
            l = pow(temp, 1/2)
            return (3.14*l*(R+r))
        elif h == None:
            return (3.14*l*(R+r))
        else:
            raise Exception("Invalid input")
    def TSA_frustum_cone(self,R,r,h,l):
        """This method returns the TSA of frustum of cone"""
        if l == None:
            temp = ((h * h) + ((R - r) * (R - r)))
            l = pow(temp, 1 / 2)
            return ((3.14 * l * (R + r))+(3.14*r*r)+(3.14*R*R))
        elif h == None:
            return ((3.14 * l * (R + r))+(3.14*r*r)+(3.14*R*R))
        else:
            raise Exception("Invalid input")
    def volume_frustum_cone(self,R,r,h,l):
        """This method returns the volume of frustum of cone"""
        if l == None:
            temp = ((h * h) + ((R - r) * (R - r)))
            l = pow(temp, 1 / 2)
            return (((1/3)*3.14*h)*((r*r)+(R*R)+(r*R)))
        elif h == None:
            return (((1/3)*3.14*h)*((r*r)+(R*R)+(r*R)))
        else:
            raise Exception("Invalid input")
    def m_cm(self,m):
        """This method converts m to cm """
        return (m*100)
    def cm_m(self,cm):
        """This method converts cm to m"""
        return (cm/100)
    def km_m(self,km):
        """This method converts km to m"""
        return (km*1000)
    def m_km(self,m):
        """This method converts m to km"""
        return (m/1000)
    def foot_inch(self,f):
        """This method converts foot to inch"""

        return (f*12)
    def inch_foot(self,i):
        """This method converts inch to foot"""
        return (i/12)
    def mm_micro_m(self,mm):
        """This method converts millimetre to micrometre"""
        return (mm*1000)
    def micro_m_mm(self,m):
        """This method converts micrometre to millimetre"""
        return (m/1000)
    def cm_mm(self,cm):
        """This method converts centimetre to millimetre"""
        return (cm*10)
    def mm_cm(self,mm):
        """This method converts millimetre to centimetre"""
        return (mm/10)
    def mile_yard(self,m):
        """This method converts miles to yard"""
        return (m*1760)
    def yard_mile(self,y):
        """This method converts yard to mile"""
        return (y/1760)
    def l_ml(self,l):
        """This method converts litre to millilitre"""
        return (l*1000)
    def ml_l(self,ml):
        """This method converts millilitre to litre"""
        return (ml/1000)
    def kg_g(self,kg):
        """This method converts kilogram to gram"""
        return (kg*1000)
    def g_kg(self,g):
        """This method converts gram to kilogram"""
        return (g/1000)
    def kg_tonne(self,kg):
        """This method converts kilogram to tonne"""
        return (kg/1000)
    def tonne_kg(self,t):
        """This method converts tonne to kilogram"""
        return (t*1000)
    def celsius_fah(self,c):
        """This method converts celsius to fahrenheit"""
        return ((c*(9/5))+32)
    def fah_celsius(self,f):
        """This method converts fahrenheit to celsius"""
        return ((f-32)*(5/9))
    def kel_celsius(self,k):
        """This method convert kelvin to celsius"""
        return (k-273.15)
    def celsius_kel(self,c):
        """This method convert celsius to kelvin"""
        return (c + 273.15 )
    def fah_kelvin(self,f):
        """This method convert fahrenheit to kelvin"""
        return ((f-32) *((5/9) + 273.15))
    def kelvin_fah(self,k):
        """This method returns kelvin to fahrenheit"""
        return ((k-273.15) * ((9/5) + 32))

    def mean_raw(self,list):
        """This method returns the mean of raw data"""
        n=len(list)
        sum=0
        for values in list:
            sum=sum+values
        return (sum/n)

    def mode_raw(self,list):

        """This method returns the mode of raw data"""
        return max(set(list), key=list.count)
    def median_raw(self,list):
        """This method returns the median of raw data"""
        temp_list=list.sort()
        n=len(temp_list)
        if n%2==0:
            temp=temp_list[(n/2)+1]
            temp2=temp_list[(n/2)+2]
            return (temp+temp2)/2

        else:
            temp=(n+1)/2
            return temp_list[temp+1]

if __name__ == '__main__':
    Mathematics=Math()















