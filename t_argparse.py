#coding:utf-8
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name" ,help="this is name", default="test_gold")
parser.add_argument("-a", "--age" ,help="this is age", default="2", type=int)
args = parser.parse_args()
print args	
