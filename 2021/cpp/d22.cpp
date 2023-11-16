#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;
using ull = unsigned long long;

struct cuboid
{
	int x0, x1, y0, y1, z0, z1;
	bool is_on;
};
vector<cuboid> cuboids;

ull solve(vector<cuboid>::const_iterator end) {
	vector<int> X, Y, Z;
	for (auto it=cuboids.cbegin(); it!=end; it++) {
		auto c = *it;
		X.push_back(c.x0);
		X.push_back(c.x1);
		Y.push_back(c.y0);
		Y.push_back(c.y1);
		Z.push_back(c.z0);
		Z.push_back(c.z1);
	}
	sort(X.begin(), X.end());
	sort(Y.begin(), Y.end());
	sort(Z.begin(), Z.end());

	auto size = X.size();
	vector<bool> grid(size*size*size, false);
	for (auto it=cuboids.cbegin(); it!=end; it++) {
		auto c = *it;
		auto i0 = distance(X.cbegin(), lower_bound(X.cbegin(), X.cend(), c.x0));
		auto i1 = distance(X.cbegin(), lower_bound(X.cbegin(), X.cend(), c.x1));
		auto j0 = distance(Y.cbegin(), lower_bound(Y.cbegin(), Y.cend(), c.y0));
		auto j1 = distance(Y.cbegin(), lower_bound(Y.cbegin(), Y.cend(), c.y1));
		auto k0 = distance(Z.cbegin(), lower_bound(Z.cbegin(), Z.cend(), c.z0));
		auto k1 = distance(Z.cbegin(), lower_bound(Z.cbegin(), Z.cend(), c.z1));

		for (auto i=i0; i<i1; i++)
		for (auto j=j0; j<j1; j++)
		for (auto k=k0; k<k1; k++)
			grid[i*size*size + j*size + k] = c.is_on;
	}

	ull total = 0;
	for (int i=0; i<X.size()-1; i++)
	for (int j=0; j<Y.size()-1; j++)
	for (int k=0; k<Z.size()-1; k++)
		if (grid[i*size*size + j*size + k]) {
			total += (ull)(X[i+1]-X[i]) * (Y[j+1]-Y[j]) * (Z[k+1]-Z[k]);
		}
	return total;
}

int main() {
	char s[4];
	int x0, x1, y0, y1, z0, z1;
	while (!feof(stdin)) {
		scanf("%s x=%d..%d,y=%d..%d,z=%d..%d\n", &s, &x0, &x1, &y0, &y1, &z0, &z1);
		cuboids.push_back({x0, x1+1, y0, y1+1, z0, z1+1, s[1]=='n'});
	}
	auto p1_end = partition(cuboids.begin(), cuboids.end(), [](const auto& c) {
			return c.x0 >= -50 && c.y0 >= -50 && c.z0 >= -50 && c.x1 <= 51 && c.y1 <= 51 && c.z1 <= 51;
		});
	printf("part 1: %lld\n", solve(p1_end));
	printf("part 2: %lld\n", solve(cuboids.cend()));
}
