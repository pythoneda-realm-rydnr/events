"""
pythoneda/realm/rydnr/events/commit_change_delegated.py

This file declares the CommitChangeDelegated event.

Copyright (C) 2023-today rydnr's pythoneda-realm-rydnr/events

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.event import Event
from pythoneda.value_object import primary_key_attribute
from typing import List

class CommitChangeDelegated(Event):
    """
    A commit change has been delegated to rydnr's realm.

    Class name: CommitChangeDelegated

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        repositoryFolder: str,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new CommitChangeDelegated instance.
        :param repositoryFolder: The cloned repository.
        :type repositoryFolder: str
        :param reconstructedId: The id of the event, if it's being reconstructed.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event is being recostructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        super().__init__(
            None, reconstructedId, reconstructedPreviousEventIds
        )
        self._repositoryFolder = repositoryFolder

    @property
    @primary_key_attribute
    def repository_folder(self) -> str:
        """
        Retrieves the folder.
        :return: Such information.
        :rtype: str
        """
        return self._repository_folder
