"""`appengine_config` gets loaded when starting a new application instance."""

import sys
import os.path


# Add `lib` subdirectory to `sys.path` to can load third-party packages.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
