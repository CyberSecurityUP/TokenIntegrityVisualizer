import tkinter as tk
from core.process_enum import ProcessEnumerator
from core.privilege_mapper import PrivilegeMapper
from core.graph_builder import GraphBuilder


class ProcessListView:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side="top", fill="both", expand=True)

        self.label = tk.Label(frame, text="Processes and Token Info")
        self.label.pack()

        self.text = tk.Text(frame, height=25, width=120)
        self.text.pack(fill="both", expand=True)

        self.refresh_button = tk.Button(frame, text="Refresh", command=self.refresh)
        self.refresh_button.pack()

        # Criar instância do grafo
        self.graph_builder = GraphBuilder()

    def refresh(self):
        self.text.delete(1.0, tk.END)
        self.graph_builder.graph.clear()  # limpar grafo a cada refresh

        processes = ProcessEnumerator.list_processes()
        for p in processes:
            self.text.insert(tk.END, f"\nPID: {p['pid']} | Name: {p['name']}\n")

            if "token" in p and "sid" in p["token"]:
                self.text.insert(tk.END, f"  SID: {p['token']['sid']}\n")

                mapped = PrivilegeMapper.map_privileges(p['token']['privileges'])
                for priv in mapped:
                    line = f"   {priv['privilege']} (Enabled={priv['enabled']}) → {priv['business_impact']}\n"
                    if priv.get("mitre"):
                        mitre = priv["mitre"]
                        line += f"      MITRE: {mitre.get('technique','N/A')} ({mitre.get('impact','N/A')})\n"

                    self.text.insert(tk.END, line)

                    # Adiciona relação no grafo (processo → privilégio)
                    self.graph_builder.add_relation(
                        p['name'],
                        priv['privilege'],
                        "Enabled" if priv["enabled"] else "Disabled"
                    )
            else:
                self.text.insert(tk.END, f"  Error: {p.get('error','No token info')}\n")

        # exportar imagem do grafo (usada pelo GraphView)
        self.graph_builder.export_png("graph.png")
        self.graph_builder.export_html("graph.html")