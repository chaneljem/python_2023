#Working with Python Lists
#!/usr/bin/env python3

# 1. Set the services variable to be an empty list
services = []

# 2. Add 'lambda', 'ec2', 'dynamodb', 's3', and 'iam' to the services list in that order without reassigning the variable
services.append('lambda')
services.append('ec2')
services.append('dynamodb')
services.append('s3')
services.append('iam')

# 3. Print the list and the length of the list
print(services)
print(len(services))

# 4. Remove two specific services from the list by name or by index
del services[0]
del services[1]

# 5. Print the new list and the new length of the list
print(services)
print(len(services))

