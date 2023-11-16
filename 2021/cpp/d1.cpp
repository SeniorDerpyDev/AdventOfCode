#include <iostream>
#include <iterator>
#include <vector>

using namespace std;

int main() {
	istream_iterator<int> start(cin), end;
	vector<int> v(start, end);

	int c = 0;
	for (int i=1; i<v.size(); i++)
		if (v[i-1] < v[i]) c++;
	cout << "part 1: " << c << "\n";

	c = 0;
	for (int i=3; i<v.size(); i++)
		if (v[i-3] < v[i]) c++;
	cout << "part 2: " << c << "\n";
}

