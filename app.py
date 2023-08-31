#!/usr/bin/env python
# coding: utf-8
import streamlit as st
def find_largest(num1, num2, num3):
    return max(num1, num2, num3)
def main():
    st.title("Find the Largest Number")
    
    num1 = st.number_input("Enter the First Number: ")
    num2 = st.number_input("Enter the Second Number: ")
    num3 = st.number_input("Enter the Third Number: ")
    
    if st.button("Find Largest"):
        largest = find_largest(num1, num2, num3)
        st.write(f"The Largest number is: {largest}")
main()

