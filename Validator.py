import time from console_progressbar import ProgressBar

pb = ProgressBar(total=100,prefix='Here', suffix='Now', decimals=3, length=50, fill='X', zfill='-')
pb.print_progress_bar(2)
time.sleep(5)
pb.print_progress_bar(25)
time.sleep(5)
pb.print_progress_bar(50)
time.sleep(5)
pb.print_progress_bar(95)
time.sleep(5)
pb.print_progress_bar(100)