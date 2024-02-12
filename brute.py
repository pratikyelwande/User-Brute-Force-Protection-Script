from datetime import datetime, timedelta

class BruteForceProtection:
    def __init__(self, max_attempts=3, lockout_duration_minutes=5):
        self.max_attempts = max_attempts
        self.lockout_duration = timedelta(minutes=lockout_duration_minutes)
        self.attempts = {}

    def check_attempts(self, ip_address):
        if ip_address in self.attempts:
            last_attempt_time = self.attempts[ip_address]
            if datetime.now() - last_attempt_time < self.lockout_duration:
                return False  # Account is locked due to too many attempts
            else:
                del self.attempts[ip_address]  # Reset attempts after lockout duration

        return True  # No lockout, proceed with login attempt

    def record_attempt(self, ip_address):
        if ip_address not in self.attempts:
            self.attempts[ip_address] = datetime.now()
        else:
            self.attempts[ip_address] = datetime.now()

brute_force_protector = BruteForceProtection()

user_ip = "192.168.0.1"
for _ in range(5):
    if brute_force_protector.check_attempts(user_ip):
        print("Login successful!")
    else:
        print("Too many login attempts. Account locked.")
        break


