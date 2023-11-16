#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n;
	string s;
	int x=0, aim=0, depth=0;
	while (cin >> s >> n) {
		if (s == "forward") {
			x += n;
			depth += n * aim;
		} else if (s == "up") {
			aim -= n;
		} else if (s == "down") {
			aim += n;
		}
	}
	cout << "part 1: " << (x * aim) << "\n";
	cout << "part 2: " << (x * depth) << "\n";
}

