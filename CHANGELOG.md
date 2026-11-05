# Changelog

Todas as mudanças relevantes do AlongFit são registradas neste arquivo.

O formato segue o [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).

## [Não publicado]

### Adicionado
- Testes automatizados com PyTest na pasta `tests/`, cobrindo as validações do `model/`, login, cadastro, estatísticas, tarefas e o cronômetro (#9).
- Medição de cobertura com `pytest-cov`, gerando `coverage.xml`, e `sonar-project.properties` para importar a cobertura no SonarCloud (#10).
- `requirements.txt` com as versões fixadas de `matplotlib` e `pygame`, e `requirements-dev.txt` com as dependências de teste (#9, #10, #15).
- Pipeline de integração contínua no GitHub Actions (`.github/workflows/ci.yml`), que roda os testes com cobertura a cada push e pull request (#16).
- Este `CHANGELOG.md` (#17).

### Alterado
- Lógica de tempo do cronômetro extraída do `SessaoController` para a classe `TempoSessao` (`model/tempo_sessao.py`), sem dependência de Tkinter. O comportamento do cronômetro não muda (#13).
- `.gitignore` completado com banco de dados, ambientes virtuais, pastas de IDE e arquivos de cobertura (#14).
- README: instalação pelo `pip install -r requirements.txt` e seção de testes (#9, #15, #16).

### Corrigido
- A tela de cadastro passa a aplicar as regras do `Usuario` (e-mail com "@" e senha com pelo menos 6 caracteres) antes de gravar no banco (#18).

### Segurança
- O sorteio do alongamento passa a usar `secrets.choice` em vez de `random.choice`, resolvendo a vulnerabilidade `python:S2245` apontada pelo SonarCloud (#12).

### Removido
- `alongfit.db` do versionamento. O banco continua sendo criado na máquina de cada pessoa no primeiro uso (#14).

## [1.0] - 2026-09-24

Versão usada como baseline da Parte 1 (tag `v1.0`, commit `c0a321b`).

### Adicionado
- Cadastro e login de usuários.
- Cartões de tarefas para configurar a jornada: tempo de trabalho, intervalo entre pausas e região de desconforto.
- Cronômetro com alertas visuais e sonoros para as pausas.
- Sugestão de alongamentos de acordo com a dor informada.
- Lembrete opcional de hidratação.
- Tela de estatísticas com gráficos (Matplotlib).
- Criação automática do banco SQLite na primeira execução, a partir dos scripts da pasta `dao/`.

[Não publicado]: https://github.com/m4lu-ricard/Alongfit_py/compare/v1.0...HEAD
[1.0]: https://github.com/m4lu-ricard/Alongfit_py/tree/v1.0
