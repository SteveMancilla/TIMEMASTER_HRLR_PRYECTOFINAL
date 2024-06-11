import unittest
from unittest.mock import patch
from src.vista.main_view import MainView

class TestMainView(unittest.TestCase):
    @patch("tkinter.simpledialog.askstring", side_effect=["Test", "User", "1234567890", "test@example.com"])
    @patch("tkinter.messagebox.showinfo")
    @patch("tkinter.messagebox.showerror")
    @patch("playsound.playsound")
    def test_timer(self, mock_playsound, mock_showerror, mock_showinfo, mock_askstring):
        app = MainView()

        # Test start timer
        app.timer_entry.insert(0, "5")
        app.start_timer()
        self.assertEqual(app.timer.get_remaining_time(), 5.0)

        # Test pause timer
        app.pause_timer()
        self.assertFalse(app.timer.is_running)

        # Test resume timer
        app.pause_timer()
        self.assertTrue(app.timer.is_running)

        # Test reset timer
        app.reset_timer()
        self.assertEqual(app.timer.get_remaining_time(), 5.0)

    @patch("tkinter.simpledialog.askstring", side_effect=["Test", "User", "1234567890", "test@example.com"])
    @patch("tkinter.messagebox.showinfo")
    @patch("tkinter.messagebox.showerror")
    @patch("playsound.playsound")
    def test_alarm(self, mock_playsound, mock_showerror, mock_showinfo, mock_askstring):
        app = MainView()

        # Test set alarm
        app.alarm_time_entry.insert(0, "23:59")
        app.set_alarm()
        self.assertTrue(app.alarm.is_set)

        # Test check alarm (simulate alarm ringing)
        app.alarm.start_time = time.time() - app.alarm.time_to_wait
        app.check_alarm()
        mock_showinfo.assert_called_with("Alarma", "¡La alarma ha sonado!")
        mock_playsound.assert_called_with("sound.mp3")

    @patch("tkinter.simpledialog.askstring", side_effect=["Test", "User", "1234567890", "test@example.com"])
    @patch("tkinter.messagebox.showinfo")
    @patch("tkinter.messagebox.showerror")
    @patch("playsound.playsound")
    def test_pomodoro(self, mock_playsound, mock_showerror, mock_showinfo, mock_askstring):
        app = MainView()

        # Test start pomodoro
        app.pomodoro_work_entry.insert(0, "0.1")
        app.pomodoro_break_entry.insert(0, "0.1")
        app.start_pomodoro()
        self.assertEqual(app.pomodoro.get_remaining_time(), 6.0)

        # Test pause pomodoro
        app.pause_pomodoro()
        self.assertFalse(app.pomodoro.is_running)

        # Test resume pomodoro
        app.pause_pomodoro()
        self.assertTrue(app.pomodoro.is_running)

        # Test reset pomodoro
        app.reset_pomodoro()
        self.assertEqual(app.pomodoro.get_remaining_time(), 6.0)

if __name__ == "__main__":
    unittest.main()
