#עמר עאצי



import os  # מייבא ספריית המערכת os
import requests  # מייבא את הספרייה requests
from bs4 import BeautifulSoup  # מייבא את פונקציות BeautifulSoup מספריית bs4

def get_website_paths(url):
    paths = set()  # יצירת קבוצת נתיבים ריקה
    try:
        response = requests.get(url)  # שליפת התגובה מה-URL
        if response.status_code == 200:  # בדיקה אם התגובה היא 200 (הכל בסדר)
            soup = BeautifulSoup(response.text, 'html.parser')  # המרת התגובה לפורמט BeautifulSoup
            for link in soup.find_all('a'):  # לולאה על כל הקישורים בדף
                href = link.get('href')  # שליפת המאפיין href של הקישור
                if href:  # בדיקה אם יש ערך ל-atribute href
                    if not href.startswith('http'):  # בדיקה אם ה-URL אינו מתחיל ב-http
                        href = url + '/' + href.lstrip('/')  # הוספת ה-URL לנתיב אם הוא אינו מתחיל ב-http
                    paths.add(href)  # הוספת הנתיב לקבוצת הנתיבים
    except Exception as e:  # תפיסת כל שגיאה כללית
        print(f"שגיאה בשליפת הנתיבים מ-{url}: {e}")  # הדפסת השגיאה
    return paths  # החזרת קבוצת הנתיבים

def download_interesting_files(url, save_dir):
    try:
        response = requests.get(url)  # שליפת התגובה מה-URL
        if response.status_code == 200:  # בדיקה אם התגובה היא 200 (הכל בסדר)
            content_type = response.headers.get('content-type')  # שליפת סוג התוכן מהכותרת של התגובה
            if content_type and ('pdf' in content_type or 'image' in content_type):  # בדיקה אם סוג התוכן הוא PDF או תמונה
                filename = os.path.join(save_dir, url.split('/')[-1])  # יצירת שם קובץ על פי ה-URL
                with open(filename, 'wb') as file:  # פתיחת הקובץ לכתיבה במצב דו-כיווני
                    file.write(response.content)  # כתיבת תוכן התגובה לקובץ
                print(f"הורדת {url} ל-{filename}")  # הדפסת הודעה על הורדת הקובץ
    except Exception as e:  # תפיסת כל שגיאה כללית
        print(f"שגיאה בהורדת הקובץ מ-{url}: {e}")  # הדפסת השגיאה

def main():
    url = input("הזן כתובת URL של האתר: ")  # קליטת ה-URL מהמשתמש
    paths = get_website_paths(url)  # קריאה לפונקציה לשליפת נתיבי האתר
    print("נתיבים שנמצאו באתר:")  # הדפסת הודעה
    for path in paths:  # לולאה על כל נתיב ברשימת הנתיבים
        print(path)  # הדפסת הנתיב

    save_dir = input("הזן תיקייה לשמירת הקבצים: ")  # קליטת התיקייה לשמירת הקבצים מהמשתמש
    if not os.path.exists(save_dir):  # בדיקה אם התיקייה אינה קיימת
        os.makedirs(save_dir)  # יצירת התיקייה אם אינה קיימת

    for path in paths:  # לולאה על כל נתיב ברשימת הנתיבים
        download_interesting_files(path, save_dir)  # קריאה לפונקציה להורדת הקבצים המעניינים

if __name__ == "__main__":
    main()  # קריאה לפונקצית ראשית
