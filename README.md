# Iniciación a la Inteligencia Artificial para ADSO – SENA 2026

Material de apoyo del curso complementario **Iniciación a la Inteligencia Artificial (23310010, 96 h)**,
SENA Centro de Comercio y Servicios, Regional Tolima. Todo se trabaja en la nube (GitHub Codespaces y Google Colab):
no hay que instalar nada en el computador y funciona en Windows, Linux y macOS.

La guía de aprendizaje completa está en [`guia/guia.pdf`](guia/guia.pdf). Cada archivo de este repositorio
corresponde a un anexo de la guía y fue probado de principio a fin en octubre de 2026.

## Contenido

| Semana | Tema | Dónde se trabaja | Archivo | Anexo |
|---|---|---|---|---|
| 1 | Programar con agentes de IA (Copilot en modo agente) | Codespaces | `main.py`, `test_main.py`, `.github/copilot-instructions.md` | C |
| 2 | Machine learning clásico con scikit-learn | Colab | [`notebooks/semana2.ipynb`](https://colab.research.google.com/github/inghggw/iniciacion-ia-adso/blob/main/notebooks/semana2.ipynb) | D |
| 3 | Deep learning y transfer learning (ViT) | Colab con GPU T4 | [`notebooks/semana3.ipynb`](https://colab.research.google.com/github/inghggw/iniciacion-ia-adso/blob/main/notebooks/semana3.ipynb) | E |
| 4 | LLM por API y RAG | Colab | [`notebooks/semana4.ipynb`](https://colab.research.google.com/github/inghggw/iniciacion-ia-adso/blob/main/notebooks/semana4.ipynb) | F |
| 5 | Servidor MCP conectado a la API | Codespaces | `servidor_mcp.py`, `probar_mcp.py`, `.vscode/mcp.json`, `.gemini/settings.json` | G |
| 6 | Fine-tuning con LoRA | Colab con GPU T4 | [`notebooks/semana6.ipynb`](https://colab.research.google.com/github/inghggw/iniciacion-ia-adso/blob/main/notebooks/semana6.ipynb) | I |

Los enlaces de los notebooks los abren directamente en Google Colab. Para guardar tus cambios usa
**Archivo → Guardar una copia en Drive**.

## Semanas 1 y 5 en Codespaces

1. En este repositorio pulsa **Code → Codespaces → Create codespace on main**.
2. En la terminal:

```bash
pip install -r requirements.txt
pytest
uvicorn main:app --reload
```

3. Semana 5: `pip install -r requirements.txt mcp` y, con la API corriendo en otra terminal, `python probar_mcp.py`.
   En el chat de Copilot usa una sesión **Local** para que vea el servidor MCP.

## Claves

Las semanas 4 y 6 usan claves gratuitas (Gemini, Groq, Hugging Face). Guárdalas como **secretos** de Colab
o de Codespaces y nunca las escribas en el código ni las subas al repositorio. Ver anexo A de la guía.
