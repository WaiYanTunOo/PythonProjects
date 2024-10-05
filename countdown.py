import time
import sys

def countdown(time_sec, show_days=True, show_progress=True):
    total_time = time_sec  # Store total time for progress tracking
    
    def format_time(time_sec):
        """Format time based on total seconds."""
        days, remainder = divmod(time_sec, 86400)
        hrs, remainder = divmod(remainder, 3600)
        mins, secs = divmod(remainder, 60)
        
        # Customize format based on whether to show days or not
        if show_days and days > 0:
            return f'{days:02}d {hrs:02}:{mins:02}:{secs:02}'
        else:
            return f'{hrs + days * 24:02}:{mins:02}:{secs:02}'  # Add days to hours if days are hidden

    def display_progress(current_time, total_time):
        """Display progress as a percentage or visual bar."""
        progress_percentage = (total_time - current_time) / total_time * 100
        bar_length = 20
        filled_length = int(bar_length * progress_percentage // 100)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        return f'[{bar}] {progress_percentage:.1f}%'

    while time_sec > 0:
        # Format time and display countdown
        time_display = format_time(time_sec)
        progress_display = display_progress(time_sec, total_time) if show_progress else ""
        
        # Combine and print the formatted string
        print(f'{time_display} {progress_display}', end='\r')
        
        time.sleep(1)  # Pause for 1 second
        time_sec -= 1  # Decrement time by 1 second

    # Completion message and beep
    print("\nTime's up! \a")  # '\a' is the bell sound (beep)

# Example usage:
countdown(10, show_days=True, show_progress=True)
