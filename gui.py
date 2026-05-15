import tkinter as tk
from tkinter import messagebox
import time
from genetic_algo import Chromosome, selection, crossover, mutate

class QueensGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FCAI-CU: 8-Queens Genetic Solver")
        self.root.configure(bg="#2c3e50")
        
        # Parameters
        self.pop_size = 100
        self.mutation_rate = 0.1
        self.running = False
        
        self.setup_ui()

    def setup_ui(self):
        # Header
        self.header = tk.Label(self.root, text="Evolutionary 8-Queens Solver", 
                               font=("Helvetica", 18, "bold"), bg="#2c3e50", fg="#ecf0f1")
        self.header.pack(pady=10)

        # Chessboard Frame
        self.board_frame = tk.Frame(self.root, bg="#34495e", bd=5, relief="sunken")
        self.board_frame.pack(pady=10)
        
        self.cells = [[None for _ in range(8)] for _ in range(8)]
        for r in range(8):
            for c in range(8):
                color = "#bdc3c7" if (r + c) % 2 == 0 else "#7f8c8d"
                cell = tk.Label(self.board_frame, text="", width=4, height=2, 
                                font=("Arial", 20), bg=color)
                cell.grid(row=r, column=c)
                self.cells[r][c] = cell

        # Stats Panel
        self.stats_label = tk.Label(self.root, text="Generation: 0 | Best Fitness: --", 
                                    font=("Courier", 12), bg="#2c3e50", fg="#f1c40f")
        self.stats_label.pack(pady=5)

        # Control Button
        self.start_btn = tk.Button(self.root, text="Start Evolution", command=self.toggle_evolution,
                                   font=("Arial", 12, "bold"), bg="#27ae60", fg="white", width=20)
        self.start_btn.pack(pady=15)

    def update_board(self, genes):
        """Maps the 8-digit chromosome to the 8x8 grid."""
        for r in range(8):
            for c in range(8):
                # Lab 8 uses 1-8 for rows, we map to 0-7 for indices
                if self.genes_to_row(genes[c]) == r:
                    self.cells[r][c].config(text="♛", fg="#c0392b")
                else:
                    self.cells[r][c].config(text="")
        self.root.update()

    def genes_to_row(self, gene_val):
        # Convert 1-8 range from lab to 0-7 range for tkinter grid
        return gene_val - 1

    def toggle_evolution(self):
        if not self.running:
            self.running = True
            self.start_btn.config(text="Running...", state="disabled")
            self.solve()
        
    def solve(self):
        # Step 1: Initial Population [cite: 1798]
        population = [Chromosome() for _ in range(self.pop_size)]
        gen = 0
        
        while self.running:
            population.sort(key=lambda x: x.fitness, reverse=True)
            best = population[0]
            
            # Step 2: Update UI with best individual [cite: 1798]
            self.update_board(best.genes)
            self.stats_label.config(text=f"Generation: {gen} | Best Fitness: {best.fitness}/28")
            
            # Termination [cite: 1806]
            if best.fitness == 28:
                messagebox.showinfo("Success", f"Solution found in {gen} generations!")
                self.running = False
                break

            # Step 3, 4, 5: Create next generation [cite: 1799, 1800, 1801]
            new_pop = [best] # Elitism
            while len(new_pop) < self.pop_size:
                p1, p2 = selection(population)
                c1, c2 = crossover(p1, p2)
                new_pop.append(mutate(c1, self.mutation_rate))
                if len(new_pop) < self.pop_size:
                    new_pop.append(mutate(c2, self.mutation_rate))
            
            population = new_pop
            gen += 1
            time.sleep(0.05) # Delay for animation effect

        self.start_btn.config(text="Start Evolution", state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = QueensGUI(root)
    root.mainloop()