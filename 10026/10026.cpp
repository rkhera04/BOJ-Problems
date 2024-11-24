#include <iostream>
#include <vector>

using namespace std;

// direction lists
int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};

// perform dfs in all directions
void dfs(vector<vector<char> >& grid, vector<vector<bool> >& visited, int x, int y, int n) {
    visited[x][y] = true;
    char currcol = grid[x][y];

    for (int i = 0; i < 4; ++i) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        
        if (nx >= 0 && ny >= 0 && nx < n && ny < n && !visited[nx][ny] && grid[nx][ny] == currcol) {
            dfs(grid, visited, nx, ny, n);
        }
    }
}

// count number of areas in the grid
int countAreas(vector<vector<char> >& grid, int n) {

    // initialize visited matrix and areas variable
    vector<vector<bool> > visited(n, vector<bool>(n, false));
    int areas = 0;
    
    // loop over n x n grid and perform dfs on nonvisited locations
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (!visited[i][j]) {
                dfs(grid, visited, i, j, n);
                // add one area for each connected region
                areas++;
            }
        }
    }

    return areas;
}

int main() {
    int n;
    cin >> n;

    // initialize n x n grid
    vector<vector<char> > grid(n, vector<char>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }
    
    // count num areas for normal vision
    int normalAreas = countAreas(grid, n);
    
    // convert the grid
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 'G') {
                grid[i][j] = 'R';
            }
        }
    }
    
    // count areas for red-green color blind vision
    int colorDeficientAreas = countAreas(grid, n);
    
    cout << normalAreas << " " << colorDeficientAreas << endl;
    
    return 0;
}
