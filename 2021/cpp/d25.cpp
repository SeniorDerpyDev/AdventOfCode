#include <iostream>
#include <iterator>
#include <vector>
#include <string>
#include <utility>

using namespace std;

int main() {
	istream_iterator<string> start(cin), end;
	vector<string> grid(start, end);

	int R = grid.size();
	int C = grid[0].size();
	int steps = 0;
	bool moved;
	do {
		moved = false;
		steps++;
		vector<string> g = grid;
		for (int r=0; r<R; r++)
			for (int c=0; c<C; c++)
				if (g[r][c] == '>' && g[r][(c+1)%C] == '.') {
					swap(grid[r][c], grid[r][(c+1)%C]);
					moved = true;
				}
		g = grid;
		for (int r=0; r<R; r++)
			for (int c=0; c<C; c++)
				if (g[r][c] == 'v' && g[(r+1)%R][c] == '.') {
					swap(grid[r][c], grid[(r+1)%R][c]);
					moved = true;
				}
	} while (moved);
	cout << "part 1: " << steps << "\n";
}

