enum week {MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY};

int main() {
  enum week today = MONDAY;
  today = WEDNESDAY;

  enum week tomorrow;
  tomorrow = today + 1;
}