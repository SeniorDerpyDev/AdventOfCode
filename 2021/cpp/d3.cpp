#include <iostream>
#include <iterator>
#include <bitset>
#include <vector>
#include <algorithm>

#define BITCOUNT 12

using namespace std;
using BitSet = bitset<BITCOUNT>;

int main() {
	istream_iterator<BitSet> start(cin), end;
	vector<BitSet> v(start, end);

	BitSet gamma;
	for (auto n=0; n<BITCOUNT; n++)
		gamma[n] = count_if(v.cbegin(), v.cend(), [=](const BitSet &bs) { return bs[n]; }) >= v.size() / 2;
	cout << "part 1: " << (gamma.to_ulong() * (~gamma).to_ulong()) << "\n";

	auto b = v.begin();
	auto e = v.end();
	int n = BITCOUNT-1;
	while (e-b > 1) {
		auto m = partition(b, e, [n](const BitSet &bs) { return bs[n]; });
		if (m-b >= e-m)
			e = m;
		else
			b = m;
		n--;
	}
	auto o2 = *b;

	b = v.begin();
	e = v.end();
	n = BITCOUNT-1;
	while (e-b > 1) {
		auto m = partition(b, e, [n](const BitSet &bs) { return bs[n]; });
		if (m-b < e-m)
			e = m;
		else
			b = m;
		n--;
	}
	auto co2 = *b;
	cout << "part 2: " << (o2.to_ulong() * co2.to_ulong()) << "\n";
}

