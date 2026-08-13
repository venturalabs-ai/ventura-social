# 📡 Como Contribuir ao Ventura Global Agents Ecosystem

Obrigado por considerar contribuir! 🎉 Este repositório faz parte do ecossistema Ventura Labs AI e seguiremos boas práticas de open source.

## 🛠️ Development Setup

### Prerequisites
- Node.js >= 20
- Git
- npm or pnpm

### 📦 Install
```bash
# Clone o repositório
git clone https://github.com/venturalabs-ai/ventura-agents.git
cd ventura-agents

# Instale dependências
npm ci

# Verifique o typecheck
npm run typecheck

# Execute os testes
npm test
```

### 🌿 Fluxo de Workflow

1. **Fork** o repositório
2. **Crie uma branch** para sua feature/correcão:
   ```bash
   git checkout -b feature/nova-funcionalidade
   # ou
   git checkout -b fix/problema-critico
   ```
3. **Crie sua feature** seguindo os padrões deste repositório
4. **Execute os testes** localmente:
   ```bash
   npm run check
   ```
5. **Commit suas mudanças** usando mensagens Conventional Commits:
   ```bash
   git commit -m "feat: adicionar nova capacidade de agente"
   # ou
   git commit -m "fix: corrigir issue de context proxy"
   ```
6. **Push para sua fork**:
   ```bash
   git push origin feature/nova-funcionalidade
   ```
7. **Abra um Pull Request** seguindo o template

## 📝 Padrões de Commits

Usamos [Conventional Commits](https://conventionalcommits.org/):

| Tipo | Exemplos |
|------|----------|
| ✨ `feat` | `feat: adicionar novo agente de RH` |
| 🐛 `fix` | `fix: corrigir vazamento de memória no context proxy` |
| 📝 `doc` | `doc: atualizar README com exemplos` |
| 🔧 `chore` | `chore: atualizar dependências` |
| 🔒 `fix` | `fix: melhorar validação de JWT` |
| ♻️ `refactor` | `refactor: reorganizar catalog de agentes` |

### Tipos de Commits Permitidos
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `doc`: Atualização de documentação
- `style`: Formatação, espaços em branco, ponto e vírgula (não afeta código)
- `refactor`: Refatoração de código, correção de bug que não afeta o comportamento
- `perf`: Melhoria de performance
- `test`: Adição de testes ausentes ou correção de testes existentes
- `build`: Mudanças no sistema de build ou dependências externas
- `ci`: Mudanças em arquivos de configuração de CI (ex: GitHub Actions)
- `chore": Atualizações gerais que não corrigem bug nem adicionam feature

## 🏗️ Guidelines de Código

### TypeScript Standards
- Use tipos estritos (`strict: true` no tsconfig)
- Evite `any` - use tipos específicos ou `unknown`
- Use interfaces para objetos, types para unions/literals
- Maximum 250 lines por arquivo (modularize quando exceder)
- Exhaustive match em switches (cube all cases)
- Named exports preferidos over default exports para bibliotecas

### Context Compression
- Mantenha 90% de redução de tokens como padrão
- Teste com `npm run check`
- Monitore métricas de consumo

### RAG Pipeline
- Use ChromaDB como vector store padrão
- Estratégias de chunking: fixed, semantic, recursive
- Hybrid search + re-ranking obrigatório
- Context assembly com token management

## 🧪 Testes

### Test Types
- **Unit tests**: Testes isolados por componente
- **Integration tests**: Testes de integração entre agentes
- **End-to-end tests**: Fluxos completos de agente

### Run Tests
```bash
npm test           # Rodar todos os testes
npm run typecheck  # Verificar types
npm run lint       # Verificar lint
npm run check      # Verificar métricas completas
```

### Test Coverage
- Mantenha cobertura mínima de 80%
- Novo código deve ter testes unitários

## 📋 Pull Request Guidelines

### PR Template
Todo PR deve seguir este modelo:
- **Descrição clara** do que foi alterado
- **Motivação** - por que essa mudança é necessária?
- **Testes** - como foi testado?
- **Checklist** - todos os itens marcados
- **Screenshots** (se applicable)

### Checklist PR
- [ ] Discussion occurred (issue filed before PR)
- [ ] Code follows project conventions
- [ ] Typecheck passes (`npm run typecheck`)
- [ ] Lint passes (`npm run lint`)
- [ ] Tests pass (`npm test`)
- [ ] Build passes (`npm run build`)
- [ ] Documentation updated (se applicable)
- [ ] No breaking changes (ou documentadas)
- [ ] License header preserved

### Revisão
- PRs requerem aprovação de um mantenedor
- Build e testes são executados automaticamente
- Conflitos devem ser resolvidos antes de merge

## 📚 Convenções

### Agent Development
- Use o manifesto YAML do agente como referência
- Siga a estrutura de 11 camadas
- Documente skills específicas
- Configure autonomy levels apropriados

### Context Compression
- Mantenha patterns consistentes
- Documente novas estratégias de compression
- Teste impactos em token usage

### Observability
- Mantenha OpenTelemetry config consistent
- Documente novas métricas
- Não quebre dashboards existentes

## 🚀 Deploy Local

```bash
# Clone
git clone https://github.com/venturalabs-ai/ventura-agents.git
cd ventura-agents

# Install
npm ci

# Build
npm run build

# Start
npm run dev

# Or use Docker Compose
docker compose up --build
```

## 🤝 Code of Conduct

Este projeto segue o [Contributor Covenant](CODE_OF_CONDUCT.md).
Por favor, leia o código de conduta completo antes de participar.

## ❓ Need Help?

- **GitHub Discussions**: Para perguntas e discussões
- **Issues**: Para bugs e feature requests
- **Email**: contato@venturalabs.ai para suporte enterprise

Obrigado por ajudar a tornar o Ventura melhor! 🚀