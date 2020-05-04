
#!/usr/bin/env python
import subprocess

src = "/home/student-02-73920f25a4f5/data/prod/"
dest = "/home/student-02-73920f25a4f5/data/prod_backup/"

def main():
  subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":
  main()
