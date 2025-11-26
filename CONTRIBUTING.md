# Contributing to MNE

Thank you for your interest in contributing to the Memory-Node Encapsulation (MNE) project! This document provides guidelines for contributing.

## Ways to Contribute

### 1. Code Contributions
- Core MNE implementation improvements
- Database adapter development (Weaviate, Neo4j, Qdrant)
- Performance optimizations
- Bug fixes
- New features

### 2. Documentation
- API documentation
- Tutorials and examples
- Use case documentation
- Translation to other languages

### 3. Research
- Experimental validation
- Benchmark comparisons
- Novel applications
- Theoretical extensions

### 4. Testing
- Unit tests
- Integration tests
- Performance tests
- Edge case identification

## Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/mne-project.git
   cd mne-project
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

5. Create a branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Code Standards

- Follow PEP 8 style guidelines
- Use type hints for function signatures
- Write docstrings for all public functions/classes
- Maintain test coverage above 80%
- Format code with Black: `black src/`
- Check with flake8: `flake8 src/`

## Testing

Run tests before submitting:
```bash
pytest tests/
pytest --cov=src tests/  # With coverage
```

## Pull Request Process

1. Update documentation for any changed functionality
2. Add tests for new features
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Submit PR with clear description of changes

## Code Review

All submissions require review. We aim to respond within 3 business days.

## Reporting Issues

Use GitHub Issues for:
- Bug reports
- Feature requests
- Documentation improvements

Please include:
- Clear description
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- System information

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Contact: brian@vector1.ai or open a discussion on GitHub.

Thank you for contributing to advancing AI memory systems!
