#!/usr/bin/env python3.7

# List starts out empty
aws_services = []

# Adding aws services using insert
aws_services.insert(0, 'EC2')
aws_services.insert(1, 'Lambda')
aws_services.insert(2, 'S3')
aws_services.insert(3, 'IAM')
aws_services.insert(4, 'Cloud9')

list_length = len(aws_services)

print("Some aws services include:" + str (aws_services), "Total listed items: " + str (list_length))

# Removing IAM and Cloud9 from the list
del aws_services[3]
del aws_services[3]

# gathering new list count
list_length = len(aws_services)

print("Now we have removed IAM and Cloud9 from the list:" + str (aws_services), "Now our total number of listed items is: " + str (list_length))
