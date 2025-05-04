from fastapi import FastAPI
import random

app = FastAPI()

side_hustles = [
    "Freelance web development",
    "Online tutoring (e.g. math, science, coding)",
    "Selling digital products on Etsy (e.g. templates, planners)",
    "Blogging with affiliate marketing",
    "Social media management for small businesses",
    "YouTube channel or content creation",
    "Graphic design on Fiverr or Upwork",
    "Virtual assistant services",
    "Print-on-demand (t-shirts, mugs, notebooks)",
    "Dropshipping store using Shopify",
    "Copywriting or editing services",
    "Resume/CV writing",
    "Voice-over work",
    "Photography gigs or selling stock photos",
    "Transcription or captioning jobs",
    "Pet sitting or dog walking",
    "Online surveys and market research",
    "App and website testing",
    "Podcasting",
    "Teaching a course on platforms like Udemy or Skillshare"
]


money_quotes = [
    "Money is a tool. Used properly it makes something beautiful; used wrong, it makes a mess. – Dave Ramsey",
    "Don’t work for money, make money work for you. – Robert Kiyosaki",
    "Too many people spend money they haven't earned to buy things they don't want to impress people they don't like. – Will Rogers",
    "The goal isn’t more money. The goal is living life on your terms. – Chris Brogan",
    "If you don't find a way to make money while you sleep, you will work until you die. – Warren Buffett",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "It’s not your salary that makes you rich, it’s your spending habits. – Charles A. Jaffe",
    "Wealth is the ability to fully experience life. – Henry David Thoreau",
    "The real measure of your wealth is how much you'd be worth if you lost all your money. – Unknown",
    "Money grows on the tree of persistence. – Japanese Proverb",
    "Success is not just making money. Success is happiness. Success is fulfillment. – Zig Ziglar"
]

@app.get("/side_hustles")

def get_side_hustle():
    """
    Returns a random side hustle idea.
    """
    
    return {
        "side_hustle":random.choice(side_hustles)
    }

@app.get("/money_qoutes")

def get_money_qoutes(apikey:str):
    """
    Returns a random money Qoute.
    """
    if apikey != "N19_Zone":
        return{
            error:"Wrong API key"
        }
    return {
        "Money_Qoute":random.choice(money_quotes)
    }