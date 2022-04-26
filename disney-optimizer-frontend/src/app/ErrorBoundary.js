import React from 'react';

export default class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: '', info: '' };
  }

  componentDidCatch(error, info) {
    // Display fallback UI
    localStorage.clear()
    this.setState({ hasError: true, error, info });
  }

  render() {
    if (this.state.hasError) {
      return (
        <div>
          {this.state.error}
          {this.state.info}
        </div>
      );
    }

    return this.props.children;
  }
}