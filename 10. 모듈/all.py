# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import veitnam
# trip_to = veitnam.VeitnamPackage()
# trip_to.detail()

# from travel import *
# trip_to = veitnam.VeitnamPackage()


from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))
print(inspect.getfile(thailand))